#include<iostream>
using namespace std;
int main()
{
    char op;
    double num1,num2;
    
    cout<<"Enter first number: ";
    cin>>num1;
    cout<<"Enter second number: ";
    cin>>num2;
    cout<<"Choose operator [+,*,-,/]: ";
    cin>>op;

    switch(op)
    {
        case '+':
        cout<<"The addition between two numbers is: "<<num1+num2<<endl;
        break;
        case '-':
        cout<<"The subtraction between two numbers is: "<<num1-num2<<endl;
        break;
        case '*':
        cout<<"The multiplication between two numbers is: "<<num1*num2<<endl;
        break;
        case '/':
        if (num2!=0)
        {
            cout<<"The divsion between two numbers is: "<<num1/num2<<endl;
        }
        else
        {
            cout<<"Error1"<<endl;
        }
        break;
        default:
        cout<<"Entered operator is invalid."<<endl;
    }
    return 0;
}
