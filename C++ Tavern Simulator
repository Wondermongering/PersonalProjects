#include <iostream>
#include <cstdlib>
#include <ctime>
#include <vector>
#include <string>

using namespace std;

// Class definitions
class Customer {
public:
    Customer(string n) : name(n) {
        // Generate a random mood for the customer
        moods = {"happy", "sad", "angry", "bored", "excited", "sleepy"};
        mood = moods[rand() % moods.size()];

        // Generate a random want for the customer
        wants = {"beer", "wine", "whiskey", "rum", "water", "juice"};
        want = wants[rand() % wants.size()];
    }
    string getName() { return name; }
    string getMood() { return mood; }
    string getWant() { return want; }
    void setDrink(string d) { drink = d; }
    string getDrink() { return drink; }
    void interactWith(Customer* c) {
        if (mood == "happy" && c->getMood() == "happy") {
            cout << name << " and " << c->getName() << " are having a great time!" << endl;
        } else if (mood == "angry" && c->getMood() == "angry") {
            cout << name << " and " << c->getName() << " are getting into a fight!" << endl;
        } else if (mood == "bored" && c->getMood() == "bored") {
            cout << name << " and " << c->getName() << " are yawning!" << endl;
        } else {
            cout << name << " and " << c->getName() << " are chatting." << endl;
        }
    }
private:
    string name;
    vector<string> moods;
    string mood;
    vector<string> wants;
    string want;
    string drink;
};

class Bartender {
public:
    void greet() { cout << "Welcome to the tavern!" << endl; }
    void serveDrink(Customer* c) {
        // Determine the drink to serve based on the customer's want
        string drink;
        if (c->getWant() == "beer") {
            drink = "a cold ale";
        } else if (c->getWant() == "wine") {
            drink = "a glass of red wine";
        } else if (c->getWant() == "whiskey") {
            drink = "a shot of whiskey";
        } else if (c->getWant() == "rum") {
            drink = "a rum and coke";
        } else if (c->getWant() == "water") {
            drink = "a glass of water";
        } else if (c->getWant() == "juice") {
            drink = "a fruity cocktail";
        } else {
            drink = "an unknown drink";
        }
        c->setDrink(drink);
        cout << "Bartender serves " << drink << " to " << c->getName() << endl;
    }
};

int main() {
    // Seed the random number generator
    srand(time(nullptr));

    // Create the bartender and greet customers
    Bartender bartender;
    bartender.greet();

    // Create some customers
    Customer customer1("Alice");
    Customer customer2("Bob");
    Customer customer3("Charlie");
    Customer customer4("Dave");
    Customer customer5("Eve");

    while (true) {
        // Prompt the user for an action
        cout << "What would you like to do? Type the number corresponding to the action and press Enter:" << endl;
cout << "1. Serve a drink to a customer" << endl;
cout << "2. Check on a customer's mood" << endl;
cout << "3. Ask a customer to leave the tavern" << endl;
cout << "4. Quit" << endl;


    int choice;
    cin >> choice;

    // Perform the chosen action
    if (choice == 1) {
        // Prompt the user to select a customer to serve a drink to
        cout << "Which customer would you like to serve a drink to? Type the number corresponding to the customer and press Enter:" << endl;
        cout << "1. " << customer1.getName() << endl;
        cout << "2. " << customer2.getName() << endl;
        cout << "3. " << customer3.getName() << endl;
        cout << "4. " << customer4.getName() << endl;
        cout << "5. " << customer5.getName() << endl;

        int customerChoice;
        cin >> customerChoice;

        // Serve a drink to the chosen customer
        if (customerChoice == 1) {
            bartender.serveDrink(&customer1);
        } else if (customerChoice == 2) {
            bartender.serveDrink(&customer2);
        } else if (customerChoice == 3) {
            bartender.serveDrink(&customer3);
        } else if (customerChoice == 4) {
            bartender.serveDrink(&customer4);
        } else if (customerChoice == 5) {
            bartender.serveDrink(&customer5);
        } else {
            cout << "Invalid choice." << endl;
        }

        // Prompt the user for the bartender's action
        cout << "What should the bartender do?" << endl;
        cout << "1. Serve a drink" << endl;
        cout << "2. Greet customers" << endl;
        cout << "3. Quit" << endl;
        cout << "Enter your choice (1-3): ";
        int bartenderChoice;
        cin >> bartenderChoice;

        // Perform the chosen action
        if (bartenderChoice == 1) {
            // Serve a drink to the chosen customer
            if (customerChoice == 1) {
                bartender.serveDrink(&customer1);
            } else if (customerChoice == 2) {
                bartender.serveDrink(&customer2);
            } else if (customerChoice == 3) {
                bartender.serveDrink(&customer3);
            } else if (customerChoice == 4) {
                bartender.serveDrink(&customer4);
            } else if (customerChoice == 5) {
                bartender.serveDrink(&customer5);
            } else {
                cout << "Invalid choice." << endl;
            }
        } else if (bartenderChoice == 2) {
            // Greet the customers
            bartender.greet();
        } else if (bartenderChoice == 3) {
            // Quit the program
            cout << "Goodbye!" << endl;
            return 0;
        } else {
            cout << "Invalid choice." << endl;
        }

    } else if (choice == 2) {
        // Prompt the user to select a customer to check on
        cout << "Which customer would you like to check on? Type the number corresponding to the customer and press Enter:" << endl;
        cout << "1. " << customer1.getName() << endl;
        cout << "2. " << customer2.getName() << endl;
        cout << "3. " << customer3.getName() << endl;


            int customerChoice;
    cin >> customerChoice;

    // Print the chosen customer's mood and want
    if (customerChoice == 1) {
        cout << customer1.getName() << " is " << customer1.getMood() << " and wants " << customer1.getWant() << endl;

    } else if (customerChoice == 2) {
        cout << customer2.getName() << " is " << customer2.getMood() << " and wants " << customer2.getWant() << endl;

    } else if (customerChoice == 3) {
        cout << customer3.getName() << " is " << customer3.getMood() << " and wants " << customer3.getWant() << endl;

    } else if (customerChoice == 4) {
        cout << customer4.getName() << " is " << customer4.getMood() << " and wants " << customer4.getWant() << endl;

    } else if (customerChoice == 5) {
        cout << customer5.getName() << " is " << customer5.getMood() << " and wants " << customer5.getWant() << endl;

    } else {
        cout << "Invalid choice." << endl;
    }

    // Prompt the user for the bartender's action
    cout << "What should the bartender do?" << endl;
    cout << "1. Serve a drink" << endl;
    cout << "2. Greet customers" << endl;
    cout << "3. Quit" << endl;
    cout << "Enter your choice (1-3): ";

    int bartenderChoice;
    cin >> bartenderChoice;

    // Perform the chosen action
    if (bartenderChoice == 1) {
        // Serve a drink to the chosen customer
        if (customerChoice == 1) {
            bartender.serveDrink(&customer1);
        } else if (customerChoice == 2) {
            bartender.serveDrink(&customer2);
        } else if (customerChoice == 3) {
            bartender.serveDrink(&customer3);
        } else if (customerChoice == 4) {
            bartender.serveDrink(&customer4);
        } else if (customerChoice == 5) {
            bartender.serveDrink(&customer5);
        } else {
            cout << "Invalid choice." << endl;
        }
    } else if (bartenderChoice == 2) {
        // Greet the customers
        bartender.greet();
    } else if (bartenderChoice == 3) {
        // Quit the program
        cout << "Goodbye!" << endl;
        return 0;
    } else {
        cout << "Invalid choice." << endl;
    }
// Pause the program
cout << "Press enter to continue...";
cin.ignore();
cin.get();
}
} // end of while loop
return 0;
}
