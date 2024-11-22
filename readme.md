# 布拉格錢數位帳本-正式啟用
English version is translated by ChatGPT. We're sorry that our English is not good enough to make sure all of the English content is right.

### 故事  Story
「衝鋒！」一向是布拉格市民面對科技發展的口號，在環境保育意識抬頭的風氣之下，當代的布拉格市長打算將當地貨幣"布拉格錢"進行數位化，運用共同帳本紀錄所有市民的財產，以減少印刷實體紙幣的數量，達到愛護環境的效果。

但是俗話說：「萬事起頭難」，帳本資料在市長以及相關部門的細心維護下還是遭到駭客竄改。你身為有關單位的一員，決定寫出程式以找出帳本出錯的源頭。

註：故事中的布拉格為虛構城市，與捷克首都布拉格並無任何關係


"Charge forward!" has always been the motto of Prague citizens in embracing technological development. In response to the growing environmental awareness, the current mayor of Prague plans to digitize the local currency, "Prague Coin," by using a shared ledger to record the assets of all citizens. This initiative aims to reduce the printing of physical banknotes and protect the environment.

However, as the saying goes, "The first step is always the hardest." Despite the mayor and related departments' meticulous maintenance, the ledger data was tampered with by hackers. As a member of the related authority, you decide to write a program to locate the source of the ledger error.

Note: The "Prague" in this story is a fictional city and has no relation to Prague, the capital of the Czech Republic.


### 布拉格錢（Block Chain）數位帳本簡介  Prague Coin (Blockchain) Digital Ledger Overview
![Block_Chain](https://github.com/fromtaoyuanhsinchuuuu/Group03-Homework/blob/main/image/Block_Chain.jpeg?raw=true)

一條區塊鏈是由數個區塊(block)組成，每個區塊內容須包含三個部份：前一個區塊的雜湊值(previous hash)、數筆資料(data)、以及特殊數字 Nonce。

previous hash 是形成鏈狀結構的關鍵。在題目中，我們假設 previous hash 是不能被任何人改變的（包括故事中竄改資料的駭客），故 previous hash 可以用來驗證前一個區塊的資料是否正確。

data 在我們的題目只會以數字的型態存在，以方便計算區塊的雜湊值(hash)，並且我們保證一個區塊至少會有一個 data。

特殊數字 Nonce 並不像前兩者一樣具有紀錄功能。Nonce 是單純用來改變區塊的雜湊值(hash)的數字，在計算區塊雜湊值的時候會被使用。本題不會要求同學藉由更改特殊數字 Nonce 來影響區塊雜湊值，所以請不要改變題目中任何區塊的 Nonce。

一個區塊的雜湊值是根據區塊內容及使用的雜湊函數決定的，在此我們將用文字檔案模擬區塊（一個文字檔案代表一個區塊）、並使用自定義的雜湊函數（詳見下方雜湊函數），進行布拉格錢數位帳本的驗證與偵錯。


A blockchain consists of several blocks. Each block contains three parts: the hash of the previous block (`previous hash`), a set of data (`data`), and a special number (`Nonce`).

The `previous hash` is the key to forming the chain structure. In this problem, we assume the `previous hash` cannot be altered by anyone (including hackers tampering with the data in the story). Thus, the `previous hash` can be used to verify whether the data in the previous block is correct.

The `data` in this problem is represented solely by numbers for easier calculation of block hashes. We guarantee that each block will have at least one data entry.

The special number `Nonce` does not have a recording function like the other two components. It is purely used to alter the block's hash value during calculations. You are not required to modify the `Nonce` value in this task.

A block's hash value is determined by its content and the hashing function used. Here, we simulate a block with a text file (one text file represents one block) and use a custom hashing function (details below) to verify and debug the Prague Coin digital ledger.


### 題目敘述  Problem Description
給定數字 $n$，代表有 $n$ 個區塊檔案 (`block_i_1.txt`, `block_i_2.txt`, ..., `block_i_n.txt`)，請檢查並驗證數位帳本中區塊的 hash 以及 previous hash 是否正確。

如果某個區塊的資料有被竄改，那麼區塊算出的 hash 與下一個區塊的 previous hash 將會不一致（忽略資料竄改後，雜湊值相同的情況），請以此為原則進行驗證。若有錯誤，請輸出第一個出錯的區塊號碼；若沒有錯誤，輸出 -1。

另外，因為最後一個區塊沒有對應的 previous hash 可供驗證，所以我們假設最後一個區塊的資料一定沒經過竄改，可以忽略。

$Hint$: 題目只要求驗證，不需要（應該也無法）修復資料，故請不要對檔案做任何寫入的動作


Given a number $n$, which represents $n$ block files (`block_i_1.txt`, `block_i_2.txt`, ..., `block_i_n.txt`), verify and validate whether the hashes and `previous hashes` in the digital ledger blocks are correct.

If a block’s data has been tampered with, the calculated hash of the block will not match the `previous hash` in the subsequent block (ignoring cases where the tampered data coincidentally results in the same hash). Verify the ledger according to this principle. If an error is found, output the index of the first faulty block. If no errors are found, output -1.

Additionally, since the last block does not have a `previous hash` for verification, assume that the last block's data has not been tampered with and can be ignored.

*Hint*: The task only requires verification. You do not need (and likely cannot) fix the data, so do not perform any write operations on the files.


### 檔案格式  File Format
檔名固定為 `block_i_j.txt`，其中 i 為測資的編號， j 為區塊的編號

檔案內容格式如下

File names follow the format `block_i_j.txt`, where i is the testcase number, and j is the block number.

File content format:
```
P: <pre-hash>
1: <data 1>
2: <data 2>
.
.
k: <data k>
N: <nonce>
```
- 第一行 P 後面的數字是 previous hash，為上一個區塊的雜湊值
    - 第一個區塊的 P 必為 0
- 最後一行 N 後面的數字是 Nonce，用以計算或改變這個區塊的雜湊值 (詳見下方雜湊函數)
    - 最後一個區塊的 Nonce 必為 0
- 剩下的部份是區塊中的 data，開頭會按照順序編號（如上方範例中 $1\ to\ k$）
    - 我們保證一個區塊至少會有一個 data
- The number after `P:` is the `previous hash` of the block, which is the hash of the previous block.
    - The `P:` of the first block will always be 0.
- The number after `N:` is the `Nonce`, used to compute or modify the block's hash value (see the hashing function below).
    - The `Nonce` of the last block will always be 0.
- The rest of the file contains the block's `data`, numbered sequentially.
    - Each block is guaranteed to have at least one data entry.

### 雜湊（Hash）函數  Hash Function
雜湊函數定義如下，將區塊的所有 data 以及 Nonce 進行運算即可得到區塊的雜湊值（不會使用到 previous hash）
- 初始 $H_0=0$
- 依照下列式子反覆運算
    - ![alt text](https://github.com/fromtaoyuanhsinchuuuu/Group03-Homework/blob/main/image/Hash_Function.jpg?raw=true)
    - 假設區塊中有 $k$ 個data，則 $i\ from\ 1\ to\ k+1$
    - $d_{k+1}$ 為區塊的 Nonce，其餘 $d_i$ 就是 \<data $i$ \>
- k+1 次運算後， $H_{k+1}$ 就是這個區塊的雜湊值

註： $\oplus$ 代表 XOR、 $\ll$ 代表邏輯左移、 $mod$ 代表取模


The hashing function is defined as follows. Compute the block's hash value by operating on all its `data` entries and the `Nonce`:
- Initial $H_0=0$ .
- Repeatedly compute using the formula:
    - ![alt text](https://github.com/fromtaoyuanhsinchuuuu/Group03-Homework/blob/main/image/Hash_Function.jpg?raw=true)
    - Assume the block contains $k$ data entries; iterate $i\ from\ 1\ to\ k+1$ .
    - $d_{k+1}$ represents the block's `Nonce`, while the remaining $d_i$ represents `<data i>`.
- After k+1 computations, $H_{k+1}$ is the hash value of the block.

Note: $\oplus$ denotes XOR, $\ll$ denotes logical left shift, and $mod$ denotes modulus.


### Input Format
第一行只有一個數字 $n$，代表有 $n$ 個區塊檔案

接著 $n$ 行是檔案名稱，block_i_j.txt ( j $from\ 1\ to\ n$ )，我們保證檔名會照順序排好

The first line contains a single integer $n$, representing the number of block files.

The next $n$ lines list the file names in sequential order:
```
n
block_i_1.txt
block_i_2.txt
.
.
.
block_i_n.txt
```


### Output Format
輸出只有一個數字

如果發現錯誤，輸出第一個出錯（號碼最小）的區塊檔案號碼

The output is a single number:

If an error is found, output the index of the first faulty block:
```
<The index of the first faulty block>
```
如果整個帳本的所有區塊檔案都沒有錯誤，輸出 -1

If all blocks pass verification, output -1
```
-1
```
題目並沒有要求同學更改檔案內容，所有檔案內容在程式執行前後必須完全相同

Do not modify the content of the files. File content must remain the same before and after program execution.


### Constrain
$1 \leq n \leq 20$

$1 \leq k \lt 1000,\ for\ all\ blocks$

$0 \leq previous\ hash,\ data,\ Nonce \lt 2^{30}$


### Taskcase Group
- **Subtask 0~6 (50 point)**
    - $1 \leq k \lt 25,\ for\ all\ blocks$
- **Subtask 7~11 (50 point)**
    - $no\ other\ constrain$

### Sample Input 1
stdin
```
3
block_0_1.txt
block_0_2.txt
block_0_3.txt
```

block_0_1.txt
```
P: 0
1: 10
2: 20
3: 31
N: 42
```

block_0_2.txt
```
P: 43
1: 15
2: 25
3: 35
N: 57
```

block_0_3.txt
```
P: 12
1: 5
2: 10
N: 0
```

### Sample Output 1
```
-1
```
此範例中所有區塊的資料數都不超過 24，所以還不會用到邏輯左移($\ll$)

區塊 1 的雜湊值為 $10\ \oplus\ 20\ \oplus\ 31\ \oplus\ 42 =43$，正好是區塊 2 的 previous hash

區塊 2 的雜湊值為 $15\ \oplus\ 25\ \oplus\ 35\ \oplus\ 57 =12$，正好是區塊 3 的 previous hash

區塊 3 為最後一個區塊，不須驗證

所有區塊都通過驗證，故輸出 -1

In this example, the number of data entries in all blocks does not exceed 24, so logical left shift is not used.

The hash of Block 1 is calculated as $10\ \oplus\ 20\ \oplus\ 31\ \oplus\ 42 =43$ , This matches the `previous hash` of Block 2.

The hash of Block 2 is calculated as $15\ \oplus\ 25\ \oplus\ 35\ \oplus\ 57 =12$ , This matches the `previous hash` of Block 3.

Block 3 is the last block and does not require verification of the `previous hash`.

Since all blocks pass verification, the output is `-1`.


### Sample Input 2
stdin
```
3
block_1_1.txt
block_1_2.txt
block_1_3.txt
```

block_1_1.txt
```
P: 0
1: 100
2: 20
3: 31
N: 42
```

block_1_2.txt
```
P: 69
1: 15
2: 25
3: 45
N: 67
```

block_1_3.txt
```
P: 12
1: 6
2: 12
N: 0
```


### Sample Output 2
```
2
```
此範例中所有區塊的資料數都不超過 24，所以還不會用到邏輯左移($\ll$)

區塊 1 的雜湊值為 $100\ \oplus\ 20\ \oplus\ 31\ \oplus\ 42 =69$，正好是區塊 2 的 previous hash

區塊 2 的雜湊值為 $15\ \oplus\ 25\ \oplus\ 45\ \oplus\ 67 = 120$，與區塊 3 的 previous hash 不同

區塊 2 並未通過驗證，故輸出 2

In this example, the number of data entries in all blocks does not exceed 24, so logical left shift is not used.

The hash of Block 1 is calculated as $100\ \oplus\ 20\ \oplus\ 31\ \oplus\ 42 =69$ , This matches the `previous hash` of Block 2.

The hash of Block 2 is calculated as $15\ \oplus\ 25\ \oplus\ 45\ \oplus\ 67 =120$ , This does not match the `previous hash` of Block 3, which is `12`.

Since Block 2 fails verification, the output is `2`.
