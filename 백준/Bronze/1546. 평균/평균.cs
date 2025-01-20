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
        var input = Console.ReadLine().Split().Select(float.Parse).ToArray();
        float maxValue = input.Max();
        //sb.AppendLine($"ToString {maxValue.ToString()}");
        for (int i = 0; i < N; i++)
        {
            input[i] = input[i] / maxValue * 100;
            //sb.AppendLine(input[i].ToString());
        }
        float result = input.Sum() / N;
        sb.Append(result);
        Console.WriteLine(sb.ToString());
    }
}
