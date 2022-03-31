using System;
using System.Collections.Generic;
using CSHexCipher;

namespace CSHexCipher {

    class Program {

        public static void Main(string[] args) {

        _start:

            try {

                Console.Write("Encrypt Or Decrypt? (E/D): ");
                char e_or_d = Convert.ToChar(Console.ReadLine());

                if (Char.ToUpper(e_or_d) == 'E') {

                    Console.Write("Message To Encrypt: ");
                    string encrypt_message = Console.ReadLine();
                    Console.Write($"Encrypted Text: {Functions.Encrypt(encrypt_message)}\nPress any key to continue...");
                    Console.ReadKey();

                } else if (Char.ToUpper(e_or_d) == 'D') {

                    Console.Write("Message To Decrypt: ");
                    string decrypt_message = Console.ReadLine();
                    Console.Write($"Decrypted Text: {Functions.Decrypt(decrypt_message)}\nPress any key to continue...");
                    Console.ReadKey();

                } else {

                    Console.Write("Please enter a valid letter (e/d) and try again!\n");
                    goto _start;

                }

            } catch (Exception ex) {

                Console.Write($"\nError: {ex.Message}");
                Console.ReadKey();

            }

        }

    }

}