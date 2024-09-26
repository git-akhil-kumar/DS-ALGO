function removeKdigits(num: string, k: number): string {
	const stack: string[] = [];
	let hashMap = new Set();

	for (const ch of num) {
		if (k > 0 && stack.length > 0 && parseInt(stack[stack.length - 1]) > parseInt(ch)) {
			k--;
			stack.pop();
		}
		stack.push(ch);
	}
	const res = stack.splice(0, stack.length - k);
	let ans = "";
	let last = true;
	for (const ch of res) {
		if (ch == "0" && last) {
			continue;
		}
		if (ch != "0") last = false;
		ans += ch;
	}
	return ans == "" ? "0" : ans;
}
