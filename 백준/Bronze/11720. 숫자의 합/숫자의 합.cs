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
        var input = Console.ReadLine();
        int result = 0;
        for (int i = 0; i < N; i++)
        {
            result += input[i] - '0';
        }
        sb.Append(result);
        Console.WriteLine(sb.ToString());
    }
}
