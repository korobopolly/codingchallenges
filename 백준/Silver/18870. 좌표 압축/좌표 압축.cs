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
        var line = Console.ReadLine().Split().Select(int.Parse).ToList();
        var uniqueNumbers = new HashSet<int>(line);

        // 정렬된 리스트 생성 (HashSet을 리스트로 변환 후 정렬)
        var sortedList = uniqueNumbers.OrderBy(x => x).ToList();

        Dictionary<int, int> indexMap = sortedList
            .Select((value, index) => new { value, index })
            .ToDictionary(pair => pair.value, pair => pair.index);

        foreach (var num in line)
        {
            sb.Append($"{indexMap[num]} ");
        }
        Console.WriteLine(sb);
    }
}
