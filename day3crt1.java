#bubblesort
import java.util.Scanner;
class Day3crt1{
    public static void bubblesort(int arr[]){
        int n=arr.length;
        for(int i=0;i<n-1;i++){
            for(int j=0;j<n-1-i;j++){
                if(arr[j]>arr[j+1]){
                    int temp=arr[j];
                    arr[j]=arr[j+1];
                    arr[j+1]=temp;
                }
            }
        }
    }
    public static void printArray(int[] arr){
        for(int val:arr)
            System.out.print(val+" ");
        System.out.println();
    }
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt();
        int arr[]=new int[n];
        for(int i=0;i<n;i++){
            arr[i]=sc.nextInt();
        }
        printArray(arr);
        bubblesort(arr);
        printArray(arr);
        
    }
}

# bubblesort is stable and it is inplace algoritham

#Insersion sort
# bubblesort is stable and it is inplace algoritham
#not sutable for large state 


#selection sort is a inplace and unstable algorithm sutable for small sets where time complexity doesnot matter 
#time compledity
#bestcase,worstcase,averagecase==bigO(n^2)


#rearrangeevenodd
publicclass RearrangeEvenOdd{
static void



#quick sort



import java.util.Scanner;
class Mainprogram{
    public static void quicksort(int[] arr,int low,int high){
        if(low<high){
            int pivotIndex=partition(arr,low,high);
            quicksort(arr,low,pivotIndex-1);
            quicksort(arr,pivotIndex+1,high);
        }
    }
    private static int partition(int[] arr,int low,int high){
        int pivot=arr[high];
        int i=low-1;
        for(int j=low;j<high;j++){
            if(arr[j]<=pivot){
                i++;
                int temp=arr[i];
                arr[i]=arr[j];
                arr[j]=temp;
            }
        }
        int temp=arr[i+1];
        arr[i+1]=arr[high];
        arr[high]=temp;
        return i+1;
    }
    public static void printArray(int[] arr){
        for(int val:arr)
            System.out.print(val+" ");
        System.out.println();
    }
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt();
        int arr[]=new int[n];
        for(int i=0;i<n;i++){
            arr[i]=sc.nextInt();
        }
        printArray(arr);
        quicksort(arr,0,n-1);
        printArray(arr);
        sc.close();
    }
}


output

6
15
2
38
10
40
44
15 2 38 10 40 44 
2 10 15 38 40 44 


# merge sort

import java.util.Scanner;

public class MergeSortProgram {

    public static void mergeSort(int[] arr, int left, int right) {
        if (left < right) {
            int mid = left + (right - left) / 2;

            mergeSort(arr, left, mid);
            mergeSort(arr, mid + 1, right);

            merge(arr, left, mid, right);
        }
    }

    private static void merge(int[] arr, int left, int mid, int right) {
        int n1 = mid - left + 1;
        int n2 = right - mid;

        int[] L = new int[n1];
        int[] R = new int[n2];

        for (int i = 0; i < n1; i++) {
            L[i] = arr[left + i];
        }

        for (int j = 0; j < n2; j++) {
            R[j] = arr[mid + 1 + j];
        }

        int i = 0, j = 0;
        int k = left;

        while (i < n1 && j < n2) {
            if (L[i] <= R[j]) {
                arr[k] = L[i];
                i++;
            } else {
                arr[k] = R[j];
                j++;
            }
            k++;
        }

        while (i < n1) {
            arr[k] = L[i];
            i++;
            k++;
        }

        while (j < n2) {
            arr[k] = R[j];
            j++;
            k++;
        }
    }

    public static void printArray(int[] arr) {
        for (int value : arr) {
            System.out.print(value + " ");
        }
        System.out.println();
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter number of elements: ");
        int n = sc.nextInt();
        int[] arr = new int[n];

        System.out.println("Enter elements:");
        for (int i = 0; i < n; i++) {j
            arr[i] = sc.nextInt();
        }

        System.out.println("Original array:");
        printArray(arr);

        mergeSort(arr, 0, n - 1);

        System.out.println("Sorted array:");
        printArray(arr);

        sc.close();
    }
}
 

output0
Enter number of elements: 5
Enter elements:
54
87
90
12
36
Original array:
54 87 90 12 36 
Sorted array:
12 36 54 87 90 



# searching
linear search is a basic and simple algorithamwith less elements to be searched



#linear search
import java