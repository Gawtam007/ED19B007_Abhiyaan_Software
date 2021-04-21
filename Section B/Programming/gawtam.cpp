#include<iostream>
using namespace std;
int main()
{
    int Arr[100],a[100],n,temp, count = 0, count1 = 0;
    cout<< "Enter number of elements : ";
    cin >> n;
    for(int i = 0; i<n ; i++)
    {
        cin >> Arr[i];
        a[i] = Arr[i];
    }

    for(int i = 0 ; i < n ; i++ )
    {
        for ( int j = 0 ; j < n-i-1 ; j++ )
        {
            if ( Arr[j] > Arr[j+1] )
            {
                temp = Arr[j];
                Arr[j] = Arr[j+1];
                Arr[j+1] = temp;
                count ++ ;
            }

            if ( a[j] < a[j+1] )
            {
                temp = a[j];
                a[j] = Arr[j+1];
                a[j+1] = temp;
                count1 ++ ;
            }

        }
    }   

    if (count < count1)
    {
        for(int i = 0; i<n ; i++)
            cout << Arr[i];
    
        cout<<"Minimum swaps required : "<< count;
    }

    else 
    {
        for(int i = 0; i<n ; i++)
        cout << a[i];

        cout<<"Minimum swaps required : "<< count1;
    }

    return 0;
}