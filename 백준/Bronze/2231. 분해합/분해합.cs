using System;
using System.Collections.Generic; //HashSet을 사용하기 위해 필요
using System.Linq; //Linq를 사용하기 위해 필요
using System.Text; // StringBuilder를 사용하기 위해 필요

class Program
{
    static void Main(string[] args)
    {
        StringBuilder sb = new StringBuilder();
        int N = int.Parse(Console.ReadLine());
        sb = new StringBuilder("0");
        for (int i = 1; i < N; i++) { 
            if (N == i + i.ToString().ToCharArray().Sum(x => x - '0'))
            {
                sb.Clear();
                sb.Append(i);
                break;
            }
        }
        Console.WriteLine(sb.ToString());
    }
}
