#include <iostream>
#include <string.h>
#include <math.h>

using namespace std;
void calculater(){
int a , b ;
char c ;
cout<<"Enter The Condation to  calculat ";
cin>>c;
cout<<" Give me The first Number ";
cin>>a;
cout<<"Give me the secound number ";
cin>>b;
if (c == '+'){
 cout<<" result is  ["<<a+b<<"]"<<endl;  
}
else if (c == '-'){
  cout<<" result is [ "<<a-b<<"]"<<endl;
} 
else if (c == '*'){
  cout<<" result is هو  [ "<<a*b<<"]"<<endl;
}
else if (c == '%'){
  cout<<" result is  [ "<<a/b<<"]"<<endl;
} 
else{
  cout<<"Eroor "<<endl;
}
  
}

void agecalculate(){
  int age;
  cout <<"Give me your date of Birth To calculte it   " ;
  cin >>age;
  
  cout<<age-2018;
  
  
  
  
}

int y = 3 ;

int main() {
 
 calculater();
 agecalculate();
 
 
 
return 0;
  
}