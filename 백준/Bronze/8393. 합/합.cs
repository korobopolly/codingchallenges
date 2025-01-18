using System;
using System.Linq;

class Program
{
    static void Main(string[] args)
    {
        int N = int.Parse(Console.ReadLine());
        int[] arr = new int[N];
        for (int i = 1; i < N+1; i++) {
            arr[i-1] = i;
        }
        Console.WriteLine(arr.Sum());
    }
}
