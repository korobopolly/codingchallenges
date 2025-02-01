using System;
using System.Collections.Generic;
using System.Text;

class Program
{
    static void Main(string[] args)
    {
        StringBuilder sb = new StringBuilder();
        var input = Console.ReadLine().Split().Select(int.Parse).ToArray();
        int N = input[0];
        int M = input[1];

        // 키로 값을 찾는 딕셔너리
        var dictionary = new Dictionary<string, int>();
        // 값으로 키를 찾는 딕셔너리
        var reverseDictionary = new Dictionary<int, string>();

        for (int i = 1; i < N + 1; i++)
        {
            string key = Console.ReadLine();
            dictionary[key] = i; // 키-값 쌍 추가
            reverseDictionary[i] = key; // 값-키 쌍 추가
        }

        for (int j = 0; j < M; j++)
        {
            string cmd = Console.ReadLine();

            if (int.TryParse(cmd, out int number))
            {
                // 값으로 키를 찾음 (O(1))
                if (reverseDictionary.TryGetValue(number, out string foundKey))
                {
                    sb.AppendLine(foundKey);
                }
            }
            else
            {
                // 키로 값을 찾음 (O(1))
                if (dictionary.TryGetValue(cmd, out int value))
                {
                    sb.AppendLine(value.ToString());
                }
            }
        }

        Console.WriteLine(sb.ToString());
    }
}