#include <iostream>
#include<stddef.h>

using namespace std;

const int MAX_ROWS = 50;

class SquareMatrix
	//멤버변수로 최대 열과행의 크기가 50인 두행열을 가지고 있다
	//멤버함수로 empty,store,add,subtract,copy를 가지고 있다
{
private:
	int matrix[50][50];
	int matrix_2[50][50];

public:
	void MakeEmpty(int); 
	// 기능 : Matrix의 n 행 열 내부를 0으로 초기화
	// 조건 : N의 최대 크기는 50
	// 결과 : N 안의 행 열은 0으로 초기화
	void StoreValue(int, int, int);
	// 기능 : Matrix의 i행 j열 내부를 value의 값으로 지정
	// 조건 : i와 j의 최대 크기는 50
	// 결과 : i행 j열 값은 value가 저장
	void Add(int matrix[50][50],int matrix_2[50][50]);
	// 기능 : 두행렬을 더한다
	// 조건 : 행과 열이 같아야만 더할 수 있다
	// 결과 : sumMatrix에 두 행렬을 더한 값이 저장된다.
	void Subtract(int matrix[50][50], int matrix_2[50][50]);
	// 기능 : 두행렬을 뺀다
	// 조건 : 행과 열이 같아야만 뺄 수 있다
	// 결과 : subMatrix에 두 행렬을 뺀 값이 저장된다.
	void Copy(int matrix[50][50], int matrix_2[50][50]);
	// 기능 : 한 행렬을 다른 행렬로 복사한다.
	// 조건 : 행과 열이 같아야만 복사 할 수 있다.
	// 결과 : 서로다른 행렬의 값이 같아진다.
};

void SquareMatrix::MakeEmpty(int n)
{
	int i, j = 0;
	for (i = 0; i < n; i++)
		for (j = 0; j < n; j++) {
			matrix[i][j] = 0;
			matrix_2[i][j] = 0;
		}	
}
void SquareMatrix::StoreValue(int i, int j, int value) {
	matrix[i][j] = value;
	matrix_2[i][j] = value;
}

void SquareMatrix::Add(int matrix[50][50],int matrix_2[50][50]) {
	int sumMatrix[50][50];
	int i, j;

	for (int i = 0; i < 50; i++) {
		for (int j = 0; j < 50; j++) {
			sumMatrix[i][j] = matrix[i][j] + matrix_2[i][j];
		}
	}
}

void SquareMatrix::Subtract(int matrix[50][50], int matrix_2[50][50]){
	int subMatrix[50][50];
	int i, j;
	for (int i = 0; i < 50; i++) {
		for (int j = 0; j < 50; j++) {
			subMatrix[i][j] = matrix[i][j] - matrix_2[i][j];
		}
	}
}
void SquareMatrix::Copy(int matrix[50][50], int matrix_2[50][50]) {
	for (int i = 0; i < 50; i++) {
		for (int j = 0; j < 50; j++) {
			matrix[i][j] = matrix_2[i][j];
		}
}
