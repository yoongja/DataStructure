int BinarySearch(int arr[], int length, int item) {
	int midPoint;
	int first = 0;
	int last = length - 1;
	bool moreToSearch = (first <= last);
	bool found = false;
	int point = -1;

	while (moreToSearch && !found) {
		midPoint = (first + last) / 2;
		if (arr[midPoint] > item) {
			last = midPoint - 1;
			moreToSearch = (first <= last);
		}
		else if (arr[midPoint] < item) {
			first = midPoint + 1;
			moreToSearch = (first <= last);
		}
		else {
			found = true;
			point = midPoint;
		}
	}
	return point; 
}
int BinarySearch_B(int arr[], int length, int item) {
	int midPoint;
	int first = 0;
	int last = length - 1;

	int point = -1;

	midPoint = (first + last) / 2;
	if (arr[midPoint] > item) {
		point = arr[midPoint + 1];
	}
	else {
		point = midPoint;
	}
	return point;
}