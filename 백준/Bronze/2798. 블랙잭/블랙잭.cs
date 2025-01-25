using System;
using System.Collections.Generic; //HashSet을 사용하기 위해 필요
using System.Linq; //Linq를 사용하기 위해 필요
using System.Text; // StringBuilder를 사용하기 위해 필요

class Program
{ 
    static void Main(string[] args)
    {
        StringBuilder sb = new StringBuilder();
        var input = Console.ReadLine().Split().Select(int.Parse).ToArray();
        var cmd = Console.ReadLine().Split().Select(int.Parse).OrderBy(x => x).ToArray();
        int N = input[0];
        int M = input[1];
        var list = new List<int>();
        for (int i = 0; i < N; i++) {
            for (int j = i + 1; j < N; j++) {
                for (int k = j + 1; k < N; k++) {
                    if (cmd[i] + cmd[j] + cmd[k] <= M)
                    {
                        list.Add(cmd[i] + cmd[j] + cmd[k]);
                    }
                }
            }
        }
        list.Sort();
        sb.Append(list[^1]);
        Console.WriteLine(sb.ToString());
    }
}
