using System;
using System.Data.SqlClient;
using System.IO;

namespace VulnerableApp
{
    class Program
    {
        // Hardcoded credentials
        private static string API_KEY = "sk-1234567890abcdef";
        
        // SQL Injection vulnerability
        public static void LoginUser(string username, string password)
        {
            string query = "SELECT * FROM Users WHERE Username='" + 
                          username + "' AND Password='" + password + "'";
            // Execute query (vulnerability present)
        }
        
        // Path traversal vulnerability
        public static string ReadFile(string filename)
        {
            string path = "/var/data/" + filename;  // No validation
            return File.ReadAllText(path);
        }
        
        static void Main(string[] args)
        {
            Console.WriteLine("Vulnerable .NET Application");
        }
    }
}
