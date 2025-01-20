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
        for (int i = 0; i < N; i++){
            var input = Console.ReadLine();
            sb.Append(input[0].ToString());
            sb.AppendLine(input[^1].ToString());
        }
        Console.WriteLine(sb.ToString());
    }
}
