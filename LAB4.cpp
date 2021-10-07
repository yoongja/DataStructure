#include <iostream>
#include "MaxItem.h"
#include "StackTType.h"
#include <vector>

using namespace std;

int main() {
	StackType<int> intStack;
	StackType<int> bStack;
	vector<int> cv;
	intStack.Push(1);
	intStack.Push(2);
	intStack.Push(3);
	intStack.Push(4);
	intStack.Push(5);
	intStack.Push(6);

	while (!intStack.IsEmpty()) {
		cv.push_back(intStack.Top());
		intStack.Pop();
	}

	for (int i = 0; i <5; i++) {
		bStack.Push(cv[i]);
	}

	while (!bStack.IsEmpty()) {
		cout<<bStack.Top();
		bStack.Pop();
	}
}