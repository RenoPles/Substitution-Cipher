using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CSHexCipher {

    class Functions {

        public static string Encrypt(string message) {

            string total_string = "";

            message.Split();

            foreach (var c in message) {

                int uni_value = Convert.ToInt32((int)c + 7);
                string add = uni_value.ToString("X");
                add = add.Remove(0, 1);

                if (c != message[message.Length - 1]) {

                    total_string += $"{uni_value.ToString("X")}-";

                } else {

                    total_string += $"{uni_value.ToString("X")}";

                }

            }

            return total_string;

        }

        public static string Decrypt(string message) {

            try {

                string total_string = "";
                string[] splitmessage = message.Split('-');

                for (int i = 0; i < splitmessage.Length; i++) {

                    string add_to_total = $"0x{splitmessage[i]}";
                    int int_add_to_total = Convert.ToInt32(add_to_total, 16) - 7;
                    total_string += Convert.ToString(Convert.ToChar(int_add_to_total))
                        ;

                }

                return total_string;

            } catch (Exception ex) {

                return $"Error: {ex.Message} Try again!";

            }

        }

    }

}
