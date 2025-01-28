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

        var people = new List<(int Age, string Name, int Rownum)>();

        for (int i = 0; i < N; i++)
        {
            var input = Console.ReadLine().Split();
            int age = int.Parse(input[0]); // 나이를 정수로 파싱
            string name = input[1];        // 이름을 저장
            int rownum = i;                // 회원가입 순번
            people.Add((age, name, rownum));       // 리스트에 추가
        }

        var sortedList = people
            .OrderBy(p => p.Age)    // 나이로 정렬
            .ThenBy(p => p.Rownum)  // 가입 순번으로 정렬
            .ToList();

        foreach (var person in sortedList)
        {
            sb.AppendLine($"{person.Age} {person.Name}");
        }
        Console.WriteLine(sb);
    }
}
