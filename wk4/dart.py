import 'dart:io';

void main() {
  // String Manipulation
  print("Enter a string:");
  String userInput = stdin.readLineSync() ?? '';

  // Demonstrating String Manipulation
  String reversedString = reverseString(userInput);
  int stringLength = userInput.length;
  String upperCaseString = userInput.toUpperCase();
  String lowerCaseString = userInput.toLowerCase();
  String substring = userInput.substring(0, (userInput.length ~/ 2));

  // Displaying results
  print("Original String: $userInput");
  print("Reversed String: $reversedString");
  print("String Length: $stringLength");
  print("Uppercase: $upperCaseString");
  print("Lowercase: $lowerCaseString");
  print("Substring (first half): $substring");

  // Collections
  List<String> stringList = [];
  Set<String> stringSet = {};
  Map<String, String> stringMap = {};

  // Adding results to collections
  stringList.add(userInput);
  stringSet.add(reversedString);
  stringMap['original'] = userInput;
  stringMap['reversed'] = reversedString;

  // Displaying collection contents
  print("List of Strings: $stringList");
  print("Set of Reversed Strings: $stringSet");
  print("Map of Strings: $stringMap");

  // File Handling
  String filePath = 'strings.txt';
  writeToFile(filePath, stringMap);

  // Date and Time
  DateTime now = DateTime.now();
  print("Current Date and Time: $now");
}

String reverseString(String input) {
  return input.split('').reversed.join('');
}

void writeToFile(String filePath, Map<String, String> data) {
  try {
    // Writing to file
    File file = File(filePath);
    String logEntry = "Timestamp: ${DateTime.now()}\n";
    data.forEach((key, value) {
      logEntry += "$key: $value\n";
    });

    // Append to the file
    file.writeAsStringSync(logEntry, mode: FileMode.append);
    print("Data written to $filePath successfully.");
  } catch (e) {
    print("Error occurred while writing to the file: $e");
  }
}