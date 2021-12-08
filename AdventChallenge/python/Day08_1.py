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

tips:
1. the two letters equal in 1, 7 give out the code for position 1 (the one left in 7)


6. position 6 is the only one not present in numbers 4 (unique) compared to 0 (the only one without
   that position)

2, 3. Pos 2 is present 2 times in segms_6, pos 3 is present 3 times

4. pos 4 is given out by the only unknown segment in 3 (the only number in segms_5 
    with all the known codes so far)

0. Given by the only segment left in number 4

5. Given by the only segment left in number 0

digits by segments

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
      if segment in code_by_pos:
         n += 1
         mis_segs.append(segment)

   return (len(encoded_number) - n, mis_segs)

import Inputs

for entry in Inputs.Day08():
   CodeByPosition = [None, None, None, None, None, None, None]
   NumbersEncoded = [None, None, None, None, None, None, None, None, None, None]

   NumsByPositions = ["012345", "23", "12456", "12346", "0236", "01346", "013456", "123", "0123456", "012346"]

   segms_6 = []
   segms_5 = []

   # TODO need to add while loop to go over the entry again and again until all numbers are done
   #      update: testing didn't show that was needed

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
         print(EncodedNumber)

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
         NumbersEncoded[3] = EncodedNumber
         break

   # pos 0
   CodeByPosition[0] = missing_segments(NumbersEncoded[4], CodeByPosition)[1][0]

   #pos 5
   CodeByPosition[5] = missing_segments(NumbersEncoded[0], CodeByPosition)[1][0]

   # map the rest of the numbers
   for enc_output in entry[1]:
      for idx, num in enumerate(NumsByPositions):
         print(enc_output, idx, num)
         if all([ch in num for ch in enc_output]):
            print(idx)
            break


   print(CodeByPosition)
   print(NumbersEncoded)
   break
