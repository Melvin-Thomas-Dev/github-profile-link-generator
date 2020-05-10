name=input("Enter file name: ")
fn='./'+str(name)+'.xlsx'
import xlrd
book=xlrd.open_workbook(fn)
sheet=book.sheet_by_index(0)
f=open('links.txt','w+')
i=1
j=int(input("Column Number which has the GitHub IDs:"))
while True:
	try:

		cell=sheet.cell(i,j-1)
		cell=str(cell)
		if 'github.com' in cell:
			cell=cell.replace('text:','')
			cell=cell.replace("'",'')
			print(cell)
			f.write(cell)
			f.write('\n')
		elif ' ' not in cell:
			cell=cell.replace('text:','')
			cell=cell.replace("'",'')
			cell='https://github.com/'+cell
			print(cell)
			f.write(cell)
			f.write('\n')
		else:
			print('Invalid input')
			f.write('Invalid input')
			f.write('\n')
		i+=1
	except IndexError:
		break

f.write(i)
f.close()

	
