using System;

class Program
{
    static void Main(string[] args)
    {
        var input = Console.ReadLine().Split();
        int H = int.Parse(input[0]);
        int M = int.Parse(input[1]);

        DateTime now = DateTime.Now;
        DateTime custumDate = new DateTime(now.Year, now.Month, now.Day, H, M, 0);

        DateTime result = custumDate.AddMinutes(-45);

        Console.WriteLine($"{result.Hour} {result.Minute}");
    }
}
