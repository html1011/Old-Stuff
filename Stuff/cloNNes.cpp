#include <iostream>
#include <vector>
#include<math.h>
using namespace std;

// I mean, like, I guess I could go ahead and translate my JS work...?
// Translations are boring... I'll just remake it!
// Ah, and yes, we should most definently do a class here!

class NN {
    public:
        int depth, width;
        vector<vector<double> > weights; /* I think it's fine to make it public...?*/ 
        void setDimensions(int, int); // Look at me! Even using the proper notation!!!
    protected: // I mean, I prefer protected over private? Then, if there are more libraries and classes, we can break it up...
        vector <vector <double> > findPartials();
        void updateWeights(vector<vector<double> >);
        vector<vector<double>> feedforwardWithInfo(vector<double>, vector<double>, vector<vector<double> >);
        double sigmoid(float);
};
vector<vector<double> > NN::feedforwardWithInfo(vector<double> inpu, vector<double> outpu, vector<vector<double> > weights)
{
    vector<vector<double> > info;
    for (int i = 0; i < weights.size(); ++i)
    {
        // info.push_back({inpu * weights[0], inpu, weights[0], NN :: sigmoid(inpu * weights[0])});
    }
}
void NN::setDimensions(int x = 2, int y = 1)
{
    depth = x; // For now, all we're doing is the depth, not width
    width = y;
}
void updateWeights(vector<vector<double> > newWeights = {{1}, {1}}) {
    // weights = newWeights; // Hmm... not sure how to get around this... Will leave it be for now...
}
vector<vector<double>> findPartials() {
    // Objective: Get the partials
}
double sigmoid(float n)
{
    1 / (1 + exp(-n));
}
int main()
{
    NN test; 
    test.setDimensions();
    cout << test.depth << test.width;
    return 0;
}