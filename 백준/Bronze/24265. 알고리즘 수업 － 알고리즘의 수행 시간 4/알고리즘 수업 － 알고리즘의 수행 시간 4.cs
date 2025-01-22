using System;
using System.Collections.Generic; //HashSet을 사용하기 위해 필요
using System.Linq; //Linq를 사용하기 위해 필요
using System.Text; // StringBuilder를 사용하기 위해 필요

class Program
{ 
    static void Main(string[] args)
    {
        StringBuilder sb = new StringBuilder();
        long n = int.Parse(Console.ReadLine());
        // i=1 -> n-1
        // i=2 -> n-2
        //...
        // i=n-1 -> 1
        //1부터 n-1까지 등차수열의 합
        //m * (m+1) / 2
        //m = n-1
        //(n-1) * n / 2

        sb.AppendLine(((n - 1) * n / 2).ToString());
        sb.AppendLine("2");
        Console.WriteLine(sb.ToString());
    }
}
