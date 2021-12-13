'''
                     positions 0 to 6
Code by position = [x, x, x, x, x, x, x]

      1
    aaaa  
   b    c 
 0 b  6 c 2
    ....  
   e    f 3
 5 e    f 
    gggg 
      4

Thought process:
1. The two segments equal in 1, 7 give out the code for position 1 (the one left in 7)

6. Position 6 is the only one not present in numbers 4 (unique) compared to 0 (the only one
   in segs_5 without a segment in that position)

2, 3. Pos 2 is present 2 times in segms_6, pos 3 is present 3 times

4. Pos 4 is given out by the only unknown segment in 3 (the only number in segms_5 
    with all the known codes so far)

0. Given by the only segment left in number 4

5. Given by the only segment left in number 0

Now we have all the positions covered with it's coded counterparts, we can crack any number
using num_to_positions() and decode_number()

Digits by segments

7 SEGMENTS: 8
6 SEGMENTS: 0, 6, 9
5 SEGMENTS: 2, 3, 5
4 SEGMENTS: 4
3 SEGMENTS: 7
2 SEGMENTS: 1
'''

def missing_segments(encoded_number, code_by_pos):
   '''Returns the ammount of missing segments at [0] and a list of those segments in [1]'''
   n = 0
   mis_segs = []
   for segment in encoded_number:
      if segment not in code_by_pos:
         n += 1
         mis_segs.append(segment)

   return (n, mis_segs)

def num_to_positions(encoded_number: str, code_by_pos):
   '''Maps the input encoded number to it's positions given the mapping given'''
   num = ""
   for ch in encoded_number:
      num += str(code_by_pos.index(ch))
   
   return num
   
def decode_number(number_by_pos, mapped_positions):
   '''Decodes a mapped number to it's int counterpart'''
   for idx, num in enumerate(mapped_positions):

      # If all characters and only those (hence the len check)
      # in the mapped positions belong to the number provided, then return
      # the index (numbers are ordered in the list)

      # Not using number_by_pos == num because they can be in different order
      if (all(ch in num and len(num) == len(num_by_pos) for ch in number_by_pos)):
         return idx

import Inputs

NumsByPositions = ["012345", "23", "12456", "12346", "0236", "01346", "013456", "123", "0123456", "012346"]
answer_count = 0


for entry in Inputs.Day08():
   CodeByPosition = [None, None, None, None, None, None, None]
   NumbersEncoded = [None, None, None, None, None, None, None, None, None, None]

   segms_6 = []
   segms_5 = []

   # First annotate which numbers have unique lengths
   for EncodedNumber in entry[0]:
      if len(EncodedNumber) == 2:
         NumbersEncoded[1] = EncodedNumber

      elif len(EncodedNumber) == 3:
         NumbersEncoded[7] = EncodedNumber

      elif len(EncodedNumber) == 4:
         NumbersEncoded[4] = EncodedNumber
   
      elif len(EncodedNumber) == 7:
         NumbersEncoded[8] = EncodedNumber

      # Then non-unique encodings
      elif len(EncodedNumber) == 6:
         segms_6.append(EncodedNumber)

      elif len(EncodedNumber) == 5:
         segms_5.append(EncodedNumber)

   # start deducing positions

   CodeByPosition[1] = [n for n in NumbersEncoded[7] if n not in NumbersEncoded[1]][0]
   
   # Pos 2 and 3
   for seg in NumbersEncoded[1]:
      n = 0
      for coded_num in segms_6:
         if seg in coded_num:
            n += 1
         
      if n == 2:
         CodeByPosition[2] = seg

      elif n == 3:
         CodeByPosition[3] = seg

   # Pos 6
   for seg in NumbersEncoded[4]:
      break_flag = False
      if not break_flag:
         if seg not in CodeByPosition:

            for coded_num in segms_6:
               if seg not in coded_num:
                  NumbersEncoded[0] = coded_num
                  break_flag = True
                  CodeByPosition[6] = seg  # d
                  break
      
   # pos 4
   for encoded_num in segms_5:
      if missing_segments(encoded_num, CodeByPosition)[0] == 1:
         CodeByPosition[4] = missing_segments(encoded_num, CodeByPosition)[1][0]
         NumbersEncoded[3] = EncodedNumber  # I think this line may be wrong
         break

   # pos 0
   CodeByPosition[0] = missing_segments(NumbersEncoded[4], CodeByPosition)[1][0]

   #pos 5
   CodeByPosition[5] = missing_segments(NumbersEncoded[0], CodeByPosition)[1][0]


   # map the output
   for enc_number in entry[1]:
      num_by_pos = num_to_positions(enc_number, CodeByPosition)
      if decode_number(num_by_pos, NumsByPositions) == 1 or \
         decode_number(num_by_pos, NumsByPositions) == 4 or \
         decode_number(num_by_pos, NumsByPositions) == 7 or \
         decode_number(num_by_pos, NumsByPositions) == 8:
         answer_count += 1

print("Answer is", answer_count)

'''
Answer is 470
'''