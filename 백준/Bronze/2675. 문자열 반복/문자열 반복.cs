using System;
using System.Collections.Generic; //HashSet을 사용하기 위해 필요
using System.Linq; //Linq를 사용하기 위해 필요
using System.Text; // StringBuilder를 사용하기 위해 필요

class Program
{
    static void Main(string[] args)
    {
        StringBuilder sb = new StringBuilder();
        var T = int.Parse(Console.ReadLine());
        for (int i = 0; i < T; i++)
        {
            var input = Console.ReadLine().Split();
            int R = int.Parse(input[0]);
            string S = input[1];
            foreach (char c in S) { 
                for (int j = 0; j < R; j++)
                {
                    sb.Append(c);
                }
            }
            sb.AppendLine();
        }
        Console.WriteLine(sb.ToString());
    }
}
