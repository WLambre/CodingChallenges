void main() {
  List<int> numbers = [74, 12, 14, 9, 7, 2, 1, 6, 3, 1, 4];
  // easy version
  numbers.sort();
  print(numbers);
  // think about it version
  print(non_dummy_sort(numbers));
}

// think about it function //
List<int> non_dummy_sort(numbers) {
  for (int i = 0; i <= numbers.length; i++) {
    if (i <= numbers[0]) {
      // basically we move every number to index: 0, if the 0th (first) element's value
      // is larger than our current value at index: i. If we moved the element,
      // we will remove it, form its original place
      numbers.insert(0, numbers[i]);
      numbers.removeAt(i);
    }
    return numbers;
  }
}
