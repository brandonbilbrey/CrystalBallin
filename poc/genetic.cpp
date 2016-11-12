#include <iostream>
#include <random>
#include <time.h>
#include <cmath>
#include <list>

using namespace std;

float randomWeight();

class Data {
  public:
    int foo;
    int bar;
    int foobar;
    int score;

    Data(int foo, int bar, int foobar, int score){
        this->foo = foo;
        this->bar = bar;
        this->foobar = foobar;
        this->score = score;
    }

    //Data(){}

    void Print(){
        cout << "foo: " << foo << "\nbar: " << bar << "\nfoobar: " << foobar << "\n";
    }
};


class Solution {
  public:
    double fooWeight;
    double barWeight;
    double foobarWeight;

    double reproduceProb;

    Data *data;

    Solution (Data *data) {
        fooWeight = randomWeight();
        barWeight = randomWeight();
        foobarWeight = randomWeight();
        this->data = data;
    }

    Solution(){}

    float getGuess() {
        return fooWeight * data->foo 
            + barWeight * data->bar
            + foobarWeight * data->foobar;
    }

    // Determines how close a Solution was to the data's actual score.
    double getFitness(){
        return 1 / abs(getGuess() - data->score);
    }

    void Print() {
        cout << "fooWeight: " << fooWeight << "\nbarWeight: " << barWeight << "\nfoobarWeight: " << foobarWeight << '\n';
        cout << "Guess: " << getGuess() << "\n\n";
    }

    bool operator ==(const Solution &b) const {
        return b.fooWeight == this->fooWeight
            && b.barWeight == this->barWeight
            && b.foobarWeight == this->foobarWeight;
    }
};


float randomWeight(){
    random_device rd;
    mt19937 gen(rd());
    uniform_real_distribution<> dis(0, 1);
    return dis(gen);

}


// Produces an offspring Solution with a 50% chance of getting either parent's genes.
static Solution Mate(Solution sol1, Solution sol2){
    srand(time(NULL));

    if(sol1.data != sol2.data)
        throw;

    Solution returnSol(sol1.data);

    returnSol.fooWeight = (rand() % 2 == 0) ? sol1.fooWeight : sol2.fooWeight;
    returnSol.barWeight = (rand() % 2 == 0) ? sol1.barWeight : sol2.barWeight;
    returnSol.foobarWeight = (rand() % 2 == 0) ? sol1.foobarWeight : sol2.foobarWeight;

    return returnSol;
}

// Mutates the the Solution's genes.
static Solution Mutate(Solution sol, double prob = .1){
    if(prob > 1 || prob < 0)
        throw;

    if(randomWeight() <= prob)
        sol.fooWeight = 1 - sol.fooWeight;
    if(randomWeight() <= prob)
        sol.barWeight = 1 - sol.barWeight;
    if(randomWeight() <= prob)
        sol.foobarWeight = 1 - sol.foobarWeight;

    return sol;
}

Solution rouletteSelect(list<Solution> sols) {
    // calculate the total weight
    double weight_sum = 0;
    for(list<Solution>::iterator it = sols.begin(); it != sols.end(); it++){
        weight_sum += it->getFitness();
    }
    // get a random value
    double value = randomWeight() * weight_sum;      
    // locate the random value based on the weights
    for(list<Solution>::iterator it = sols.begin(); it != sols.end(); it++){
        value -= it->getFitness();             
        if(value <= 0) return *it;
    }
    // when rounding errors occur, we return the last item's index 
    return sols.back();
}

// Takes an array of Solutions and mates the best solutions to create a new generation.
static list<Solution> getNewGen(list<Solution> parents){
    list<Solution> children;
    for(int i = 0; i < parents.size(); i ++){
        Solution parent1;
        Solution parent2;

        do{
            parent1 = rouletteSelect(parents);
            parent2 = rouletteSelect(parents);
        }while(parent1 == parent2);

        Solution child = Mate(parent1, parent1);

        children.push_back(Mutate(child));
    }

    return children;
}


int main(){
    Data data(12, 33, 99, 35);
    list<Solution> solutions;

    // Generate random solutions.
    for(int i = 0; i < 10; i ++)
        solutions.push_back(Solution(&data));

    for(int i = 0; i < 1000000; i ++){
        cout << "Generation " << i << '\n';
        cout << "-------------------------\n";
        // Set their fitness.
        for(list<Solution>::iterator it = solutions.begin(); it != solutions.end(); it++){
            it->Print();

            if(it->getGuess() == data.score){
                string dummy;
                cout << "Hell yeah!\n";
                cin >> dummy;
            }
        }

        // Get new generation.
        solutions = getNewGen(solutions);
    }
}
