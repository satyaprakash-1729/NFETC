import sys
import json

def main():
       infile = sys.argv[1]
       outfile = sys.argv[2]

       sentence_list = {}
       with open(infile) as input_file:
              lines = input_file.readlines()
              for line in lines:
                     cols = line.strip().split('\t')
                     start = cols[0]
                     end = cols[1]
                     sentence = cols[2]
                     labels = cols[3]
                     features = cols[4]
                     if(sentence in sentence_list):
                            sentence_list[sentence]["mentions"].append(
                                          {
                                          "start": start,
                                          "labels": labels.strip().split(),
                                          "end": end,
                                          "features": features.strip().split()
                                          }
                                   )
                     else:
                            sentence_list[sentence] = {
                            "tokens": sentence.strip().split(),
                            "mentions": [
                                          {
                                          "start": start,
                                          "labels": labels.strip().split(),
                                          "end": end,
                                          "features": features.strip().split()
                                          }
                                   ]
                            }
       with open(outfile, 'w') as output_file:
              data_to_write = []
              for sentence in sentence_list:
                     data_to_write.append(sentence_list[sentence])
              json.dump(data_to_write, output_file)

if __name__ == "__main__":
       main()
