#include <iostream>
#include <string>

using namespace std;

string addStrings(string num1, string num2)
{
    string result = "";
    int carry = 0;
    int i = num1.size() - 1;
    int j = num2.size() - 1;

    while (i >= 0 || j >= 0)
    {
        int sum = carry;
        if (i >= 0)
        {
            sum += num1[i] - '0';
            i--;
        }
        if (j >= 0) {
            sum += num2[j] - '0';
            j--;
        }
        result = to_string(sum % 10) + result;
        carry = sum / 10;
    }

    if (carry > 0)
    {
        result = to_string(carry) + result;
    }

    return result;
}

int main() {
    string num1, num2;
    cout << "Enter the first large integer: ";
    cin >> num1;
    cout << "Enter the second large integer: ";
    cin >> num2;
    string sum = addStrings(num1, num2);
    cout << "Sum = " << sum << endl;
    return 0;
}