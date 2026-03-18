"""
Convert plain text files into Ducky Script payload files
Usage: python txt_to_payload.py input.txt 
"""

import sys
import os

def txt_to_payload(input_file, output_file=None):
    """
    Convert a text file into a Ducky Script payload.
    
    Each line of text becomes a STRING command followed by ENTER.
    Blank lines in the input file become additional ENTER commands.
    """
    
    if not os.path.exists(input_file):
        print(f"Error: Input file '{input_file}' not found")
        return False
    
    # Default output filename
    if output_file is None:
        output_file = "payload.dd"
    
    try:
        with open(input_file, 'r', encoding='utf-8') as infile:
            lines = infile.readlines()
        
        with open(output_file, 'w', encoding='utf-8') as outfile:
            # Add HID detection at the start
            outfile.write("PASSIVE_WINDOWS_DETECT\n")
            outfile.write("\n")
            
            for line in lines:
                line = line.rstrip('\n\r')  # Remove newline characters
                
                # If line is empty, write ENTER only
                if not line.strip():
                    outfile.write("ENTER\n")
                    outfile.write("DELAY 50\n")
                    continue
                
                # Write STRING command + ENTER for non-empty lines
                outfile.write(f"STRING {line}\n")
                outfile.write("ENTER\n")
                outfile.write("DELAY 50\n")
            
            outfile.write("\n")
            outfile.write("REM Payload complete\n")
        
        print(f"✓ Successfully created: {output_file}")
        print(f"  Processed {len(lines)} lines")
        return True
        
    except Exception as e:
        print(f"Error: {e}")
        return False

def txt_to_payload_custom(input_file, output_file=None, string_delay=50, enter_delay=50):
    """
    Convert text file to payload with custom delays.
    Each line gets STRING + ENTER.
    Blank lines get just ENTER.
    """
    
    if not os.path.exists(input_file):
        print(f"Error: Input file '{input_file}' not found")
        return False
    
    if output_file is None:
        output_file = "payload.dd"
    
    try:
        with open(input_file, 'r', encoding='utf-8') as infile:
            lines = infile.readlines()
        
        with open(output_file, 'w', encoding='utf-8') as outfile:
            outfile.write("PASSIVE_WINDOWS_DETECT\n\n")
            
            for line in lines:
                line = line.rstrip('\n\r')
                
                if not line.strip():
                    # Blank line = just ENTER
                    outfile.write("ENTER\n")
                    outfile.write(f"DELAY {enter_delay}\n")
                else:
                    # Non-blank line = STRING + ENTER
                    outfile.write(f"STRING {line}\n")
                    outfile.write("ENTER\n")
                    outfile.write(f"DELAY {string_delay}\n")
            
            outfile.write("\nREM Payload complete\n")
        
        print(f"✓ Successfully created: {output_file}")
        print(f"  Processed {len(lines)} lines")
        return True
        
    except Exception as e:
        print(f"Error: {e}")
        return False

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python txt_to_payload.py input.txt [output.dd]")
        print("\nExamples:")
        print("  python txt_to_payload.py commands.txt")
        print("  python txt_to_payload.py mytext.txt custom_payload.dd")
        print("\nFeature:")
        print("  Each line gets STRING + ENTER")
        print("  Blank lines become additional ENTERs")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else None
    
    txt_to_payload(input_file, output_file)