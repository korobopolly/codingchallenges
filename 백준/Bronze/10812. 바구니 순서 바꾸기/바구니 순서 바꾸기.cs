using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

class Program
{
    static void Main(string[] args)
    {
        var cmd = Console.ReadLine().Split().Select(int.Parse).ToArray();
        int N = cmd[0];
        int M = cmd[1];
        var list = new List<int>();
        for (int o = 1; o < N + 1; o++)
        {
            list.Add(o);
        }
        for (int p = 0; p < M; p++)
        {
            var input = Console.ReadLine().Split().Select(int.Parse).ToArray();
            int i = input[0] - 1;
            int j = input[1] - 1;
            int k = input[2] - 1;
            RotateListSegment(list, i, j, k);
        }
        for (int i = 0; i < list.Count(); i++) {
            Console.Write($"{list[i]} ");
        }
    }

    static void RotateListSegment(List<int> list, int start, int end, int pivot)
    {
        List<int> firstPart = list.GetRange(start, pivot - start); // pivot 이전 부분
        List<int> secondPart = list.GetRange(pivot, end - pivot + 1); // pivot 부분

        int index = start;
        foreach (var num in secondPart)
            list[index++] = num;
        foreach (var num in firstPart)
            list[index++] = num;
    }
}