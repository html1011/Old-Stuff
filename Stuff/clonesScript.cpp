#include <iostream>
#include <fstream>
#include <vector>
#include <string>
// I mean, I'm assuming we'll be using fstream for, like, reading the files and everything...
using namespace std;

// Hey, Sarah... do you want to use a CLASS???

// All the functions we plan to use:
/*vector<vector<string> >*/ void lexer(vector<string>); 
// The output format: {{"token", "value"}, {"token", "value"}, ... , {"token", "value"}};
// The input is just a vector of each line? I'm doing each line because it seems easier... I'll work for now till you show up...

void /*vector<vector<string> >*/ lexer(vector<string> code) {
    // So... we can't quite use a .split as far as I can tell... Let's do it more basically...
    // Um... I sort of want you when determining the syntax...
    for (int i = 0; i < code.size(); ++i) {
        cout << code[i];
    }
    vector<vector<string> > key = {{"variable", "set", "sar"}, {"function", ""}};
}

int main() {
    vector<string> code;
    string path, data;
    cout << "Enter the file path: ";
    cin >> path;
    ifstream fin(path);
    while (getline(fin, data)) {
        // cout << data << endl;
        code.push_back(data);
    }
    lexer(code);
    // for (int i = 0; i < code.size(); ++i) cout << code[i] << endl;
}

/*
I'm not as fluent in bash as you, so you'll have to walk me through it.
What'd you do? For what? That's really, really cool!
It's a read-only terminal? 
cin >> okay;
It's alright; I'm pretty bad at bash as well, so this could be interesting.... I just know that it's possible and that I've done something kind of similar before.
I created an alias... I think it literally just did the exact same thing as cd.
&#9786;
1 Hello? Heeeeeellooooooooooooooo?
cin >> ShreyaOkay;
Yes. And you?
Okay, can you write in the terminal?
Okay.
I'm going to start by figuring it out in the terminal first, then moving on to making it a bash file.
I think we use cat?
Oh! So cat == bash. (Mac v. Linux). That's cool... Okay.
I think we use bash to execute it, though usually I use sh.
Okay. In Linux, do you have to type in "bash" to get into it?
Good? 1. 
Yep. Go ahead?
*/