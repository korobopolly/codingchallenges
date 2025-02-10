using System;
using System.Collections.Generic;
using System.Linq;
using System.Runtime.InteropServices;
using System.Text;

class Program2
{
    static void Main(string[] args)
    {
        // 첫 번째 줄 입력 (필요한 경우 사용)
        var input = Console.ReadLine().Split().Select(int.Parse).ToArray();
        int A = input[0];
        int B = input[1];
        int C = input[2];

        var cmd1 = Console.ReadLine().Split().Select(int.Parse).ToArray();
        var cmd2 = Console.ReadLine().Split().Select(int.Parse).ToArray();
        var cmd3 = Console.ReadLine().Split().Select(int.Parse).ToArray();

        var list1 = Enumerable.Range(cmd1[0], cmd1[1] - cmd1[0]).ToList();
        var list2 = Enumerable.Range(cmd2[0], cmd2[1] - cmd2[0]).ToList();
        var list3 = Enumerable.Range(cmd3[0], cmd3[1] - cmd3[0]).ToList();

        var mergedList = list1.Concat(list2).Concat(list3).ToList();

        int result = 0;

        var countDictionary = new Dictionary<int, int>();
        foreach (var item in mergedList)
        {
            if (countDictionary.ContainsKey(item))
            {
                countDictionary[item]++;
            }
            else {
                countDictionary[item] = 1;
            }
        }

        foreach (var kvp in countDictionary)
        {
            if (kvp.Value == 1) { result += kvp.Value * A; }
            else if (kvp.Value == 2) { result += kvp.Value * B; }
            else { result += kvp.Value * C; }
        }

        Console.WriteLine(result);
    }
}