#include <iostream>

using namespace std;

const int MAX_ITEMS = 200;
class doublestack
{
private:
	int top_small; //1000보다 작거나 같은 스택의 top
	int top_big; // 1000보다 큰 스택의 top
	int items[MAX_ITEMS];
public:
	void Push(int item); //C에서 구현할 push 연산
	void Print(); //stack 의 상황을 보여줄 수 있는 함수(채점시)
	
};

void doublestack::Push(int c) {
top_small = 0;
top_big = 199;
	while(top_small != top_big){
		if (c <= 1000) {
			items[top_small] = c;
			top_small++;
		}
		else {
			items[top_big] = c;
			top_big--;
		}
	}
}
void doublestack::Print() {
	for (int i = 0; i < 200; i++)
		cout << items[i];
}

int main() {
	return 0;
}