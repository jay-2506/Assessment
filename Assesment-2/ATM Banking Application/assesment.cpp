// Simple ATM Banking Program in C++
#include <iostream>
#include <ctime>
using namespace std;

// Constant PIN and starting balance
const int PIN = 12345;
int balance = 20000;

// Function to show welcome screen with date/time
void showWelcome() {
    time_t now = time(0);
    char* dt = ctime(&now);
    cout << "===============================\n";
    cout << "  Welcome to ATM Banking App\n";
    cout << "  Date & Time: " << dt;
    cout << "===============================\n";
}

// Function to show help screen
void showHelp() {
    cout << "\n===== HELP MENU =====\n";
    cout << "1. Insert card\n";
    cout << "2. Enter PIN (12345)\n";
    cout << "3. Use options to manage account\n";
    cout << "4. Contact bank for support\n";
    cout << "======================\n";
}

// Function to deposit money
void deposit() 
{
    int amount;
    cout << "\nEnter amount to deposit: ";
    cin >> amount;
    balance += amount;
    cout << "Amount deposited. Current balance: Rs. " << balance << "\n";
}

// Function to withdraw money
void withdraw() 
{
    int amount;
    cout << "\nEnter amount to withdraw: ";
    cin >> amount;
    if (amount > balance) {
        cout << "Insufficient funds. Cannot withdraw.\n";
    } else {
        balance -= amount;
        cout << "Withdrawal successful. Remaining balance: Rs. " << balance << "\n";
    }
}

// Function to check balance
void checkBalance()
 {
    cout << "\nCurrent account balance: Rs. " << balance << "\n";
}

// Main function
int main() 
{
    showWelcome();
    int choice;

    cout << "\n1. Login\n2. Help\nEnter your choice: ";
    cin >> choice;

    if (choice == 1)
     {
        int userPin;
        cout << "\nEnter your PIN: ";
        cin >> userPin;

        if (userPin == PIN) 
        {
            int option;
            do
             {
                cout << "\n===== MENU =====\n";
                cout << "1. Deposit\n2. Withdraw\n3. Check Balance\n4. Exit\n";
                cout << "Enter your option: ";
                cin >> option;

                if (option == 1) deposit();
                else if (option == 2) withdraw();
                else if (option == 3) checkBalance();
                else if (option == 4) cout << "\nThank you for using the ATM!\n";
                else cout << "Invalid option.\n";
            } while (option != 4);
        } 
        else 
        {
            cout << "\nWrong PIN. Exiting.\n";
        }
    }
     else if (choice == 2)
     {
        showHelp();
    } 
    else
     {
        cout << "\nInvalid choice. Exiting.\n";
    }

    return 0;
}