using System;

class Program
{
    static void Main(string[] args)
    {
        Console.WriteLine("Hello, World!");
        
        // 사용자 입력 받기
        Console.Write("이름을 입력하세요: ");
        string name = Console.ReadLine();
        
        Console.WriteLine($"안녕하세요, {name}님!");
    }
}
