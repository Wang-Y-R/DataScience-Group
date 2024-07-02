根据测试报告，软件在添加群组成员功能上存在以下问题：

1. **添加成员上限提示不明确**：用户在选择超过20个成员时，系统未及时提示已超过上限，而是在用户提交创建群组后才提示“数据超过系统限制”。这种设计使用户在不知情的情况下继续操作，导致不必要的重复劳动。

2. **添加成员上限提示时机不当**：系统应在用户选择超过20个成员时立即给出提示，而不是在提交创建群组后才提示。这使用户能够及时调整操作，避免无效操作。

3. **添加成员上限提示信息不具体**：提示信息只显示“数据超过系统限制”，未明确指出是成员数量超过20人的限制。这导致用户难以理解错误原因，应明确提示“超过成员上限20人”。

4. **添加成员上限控制不严格**：系统允许用户选择超过20个成员，但在提交时才提示错误，未在用户选择时就限制数量。这导致用户在选择时存在困惑。

5. **添加成员上限提示缺乏友好性**：提示时机和内容的设计不够友好，增加了用户的操作成本，影响用户体验。

综上所述，软件在添加群组成员功能上存在交互设计缺陷，提示时机和内容不明确，需要优化提示时机、提示内容和数量控制，以提高用户体验。