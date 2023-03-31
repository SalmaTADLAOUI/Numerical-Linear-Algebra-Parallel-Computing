#include <stdio.h>

#define ROWS_A 3
#define COLS_A 4
#define ROWS_B 4
#define COLS_B 2

void multiply_matrices(int A[][COLS_A], int B[][COLS_B], int C[][COLS_B]) {
  for (int i = 0; i < ROWS_A; i++) {
    for (int j = 0; j < COLS_B; j++) {
      int sum = 0;
      for (int k = 0; k < ROWS_B; k++) {
	sum += A[i][k] * B[k][j];
      }
      C[i][j] = sum;
    }
  }
}

int main() {
  int A[ROWS_A][COLS_A] = {{1, 2, 3, 4}, {5, 6, 7, 8}, {9, 10, 11, 12}};
  int B[ROWS_B][COLS_B] = {{1, 0}, {0, 1}, {1, 1}, {1, 1}};
  int C[ROWS_A][COLS_B];

  multiply_matrices(A, B, C);

  // print the result
  for (int i = 0; i < ROWS_A; i++) {
    for (int j = 0; j < COLS_B; j++) {
      printf("%d ", C[i][j]);
    }
    printf("\n");
  }

  return 0;
}
