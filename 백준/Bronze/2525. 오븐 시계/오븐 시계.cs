using System;

class Program
{
    static void Main(string[] args)
    {
        var input = Console.ReadLine().Split();
        int H = int.Parse(input[0]);
        int M = int.Parse(input[1]);
        int duration = int.Parse(Console.ReadLine());

        // 오늘 날짜를 기준으로 'H시 M분'을 만든 뒤, 45분 빼기
        DateTime result = DateTime.Today
            .AddHours(H)
            .AddMinutes(M + duration);

        Console.WriteLine($"{result.Hour} {result.Minute}");
    }
}
