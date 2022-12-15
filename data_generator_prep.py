from video_capture import *
from image_generator import *
from image_rescaling import *
from image_Agumentation import *
import json
main_dir='/media/sahitya/OS/10_sec/data'
def prep():
    perm=int(input('How many objects or class:'))
    person_list={}
    person_dir_path={}
    n=int(input('How many image You want to create by Agumentation :'))
    for i in range(1,perm+1):
        person=input('Enter name of object:')
        person_list[person]=i
        person_data=os.path.join(main_dir,person)
        person_dir_path[person]=person_data
        os.mkdir(person_data)
        print('Show _objects---------------')
        video_generator(person_data,person)
        image_generator(person_data,person)
        image_rescaling(person_data)
        
        data_agumentation(person_data,n)
    
    def ratio_train(n):
        return int((80/100)*n)
    def ratio_val(n):
        return int((20/100)*n)

    train_data=os.path.join(main_dir,'train')
    os.mkdir(train_data)
    val_data=os.path.join(main_dir,'val')
    os.mkdir(val_data)
    print('Dividing directories : -----------------------------------')
    for key,path in person_dir_path.items():
        class_train_path=os.path.join(train_data,key)
        os.mkdir(class_train_path)
        for i,img in enumerate(os.listdir(path)):
            source=os.path.join(path,img)
            shutil.move(source,class_train_path)
        class_val_path=os.path.join(val_data,key)
        os.mkdir(class_val_path)
        for img in random.sample(os.listdir(class_train_path),ratio_val(len(os.listdir(class_train_path)))):
            source=os.path.join(class_train_path,img)
            shutil.move(source,class_val_path)

    labels={}
    for key,path in person_dir_path.items():
        dir_paths=os.path.join(train_data,key)
        labels[key]=np.full(len(os.listdir(dir_paths)),person_list[key])

    dir_class_img={}
    for key,path in person_dir_path.items():
        dir_paths=os.path.join(train_data,key)
        img_dict={}
        for i,img in enumerate(os.listdir(dir_paths)):
            img_pi = Image.open(os.path.join(dir_paths,img))
            arr_img=np.asarray(img_pi)
            img_dict[i]=arr_img.flatten()
        dir_class_img[key]=img_dict
    print('Creating  DataFrames : ----------------------(data.csv)')
    data=pd.DataFrame()
    lab_data=pd.DataFrame()
    for (key1,values),(lab_key,lab_values) in zip(dir_class_img.items(),labels.items()):
        temp_df=pd.DataFrame(values)
        temp_df=temp_df.T
        data=pd.concat([data,temp_df],axis=0)
        lab_data_temp=pd.DataFrame(lab_values)
        lab_data=pd.concat([lab_data,lab_data_temp],axis=0)  
    final_data_set=pd.concat([data,lab_data],axis=1)
    final_data_set = final_data_set.apply(np.random.permutation, axis=0)    
    final_data_set.to_csv('/media/sahitya/OS/10_sec/csv_data/data.csv',index=False)
    label_data=pd.DataFrame(labels)
    label_data.to_csv('classes.text',index=False)
    out_file = open('classes.json','w+')
    json.dump(person_list,out_file)

