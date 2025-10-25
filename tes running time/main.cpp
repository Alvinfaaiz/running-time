#include <iostream>
#include <chrono>
#include <iomanip>
#include <cstdlib>
#include <ctime>

using namespace std;
using namespace chrono;

long long operasiIteratif = 0;
long long operasiRekursif = 0;

// Selection Sort Iteratif
void selectionSortIteratif(int arr[], int n) {
    operasiIteratif = 0;

    for (int i = 0; i < n - 1; i++) {
        int minIdx = i;
        operasiIteratif++;

        for (int j = i + 1; j < n; j++) {
            operasiIteratif++;
            if (arr[j] < arr[minIdx]) {
                minIdx = j;
                operasiIteratif++;
            }
        }

        // Swap
        if (minIdx != i) {
            int temp = arr[i];
            arr[i] = arr[minIdx];
            arr[minIdx] = temp;
            operasiIteratif += 3;
        }
    }
}

int findMinIndex(int arr[], int start, int end) {
    if (start == end) {
        return start;
    }

    int minIdx = findMinIndex(arr, start + 1, end);
    operasiRekursif++;

    return (arr[start] < arr[minIdx]) ? start : minIdx;
}

void selectionSortRekursif(int arr[], int n, int index = 0) {
    if (index == n - 1) {
        return;
    }

    operasiRekursif++;
    int minIdx = findMinIndex(arr, index, n - 1);

    // Swap
    if (minIdx != index) {
        int temp = arr[index];
        arr[index] = arr[minIdx];
        arr[minIdx] = temp;
        operasiRekursif += 3;
    }

    selectionSortRekursif(arr, n, index + 1);
}

void generateRandomArray(int arr[], int n) {
    for (int i = 0; i < n; i++) {
        arr[i] = rand() % 10000;
    }
}

void copyArray(int source[], int dest[], int n) {
    for (int i = 0; i < n; i++) {
        dest[i] = source[i];
    }
}

void printArray(int arr[], int n) {
    for (int i = 0; i < n; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;
}

int main() {
    srand(time(0));

    int n;

    cout << "Masukkan jumlah elemen array (n): ";
    cin >> n;

    // Alokasi array
    int* originalArray = new int[n];
    int* arrayIteratif = new int[n];
    int* arrayRekursif = new int[n];

    generateRandomArray(originalArray, n);

    cout << "\n--- Data Array ---\n";
    cout << "Array awal: ";
    printArray(originalArray, n);

    // Test Selection Sort Iteratif
    copyArray(originalArray, arrayIteratif, n);
    auto startIteratif = high_resolution_clock::now();
    selectionSortIteratif(arrayIteratif, n);
    auto endIteratif = high_resolution_clock::now();
    auto durasiIteratif = duration_cast<duration<double>>(endIteratif - startIteratif);

    // Test Selection Sort Rekursif
    operasiRekursif = 0;
    copyArray(originalArray, arrayRekursif, n);
    auto startRekursif = high_resolution_clock::now();
    selectionSortRekursif(arrayRekursif, n);
    auto endRekursif = high_resolution_clock::now();
    auto durasiRekursif = duration_cast<duration<double>>(endRekursif - startRekursif);

    if (n <= 20) {
        cout << "\nArray setelah sorting (Iteratif): ";
        printArray(arrayIteratif, n);

        cout << "Array setelah sorting (Rekursif): ";
        printArray(arrayRekursif, n);
    }

    cout << "\n=================================================\n";
    cout << "              HASIL ANALISIS                     \n";
    cout << "=================================================\n\n";

    cout << fixed << setprecision(6);

    // Selection Sort Iteratif
    cout << "SELECTION SORT ITERATIF:\n";
    cout << "  Waktu eksekusi    : " << durasiIteratif.count() << " detik\n";
    cout << "  Jumlah operasi    : " << operasiIteratif << "\n";
    cout << "  Kompleksitas      : O(n^2) = O(" << n << "^2) = " << (n * n) << "\n";

    cout << "\nSELECTION SORT REKURSIF:\n";
    cout << "  Waktu eksekusi    : " << durasiRekursif.count() << " detik\n";
    cout << "  Jumlah operasi    : " << operasiRekursif << "\n";
    cout << "  Kompleksitas      : O(n^2) = O(" << n << "^2) = " << (n * n) << "\n";


    // Dealokasi memori
    delete[] originalArray;
    delete[] arrayIteratif;
    delete[] arrayRekursif;

    return 0;
}
