#include <map>
#include <string>
#include <iostream>

enum StringValue {norm_label,
                  norm_label_2,
                  norm_label_3,
                  norm_label_4,
                  norm_label_5,
                  norm_label_6,
                  norm_label_7,
                  norm_label_8,
                  norm_label_9,
                  norm_spinBox_10,
                  norm_spinBox_11,
                  norm_spinBox_12,
                  norm_spinBox_13,
                  norm_spinBox_14,
                  norm_spinBox_15,
                  norm_spinBox_16
                 };
static std::map<std::string, StringValue> s_mapStringValues;
static char szInput[_MAX_PATH];
static void Initialize();

int main(){
    Initialize();
    switch (s_mapStringValues[szInput]){
    case norm_label:
    case norm_label_2:
    case norm_label_3:
    case norm_label_4:
    case norm_label_5:
    case norm_label_6:
    case norm_label_7:
    case norm_label_8:
    case norm_label_9:
    case norm_spinBox_10:
    case norm_spinBox_11:
    case norm_spinBox_12:
    case norm_spinBox_13:
    case norm_spinBox_14:
    case norm_spinBox_15:
    case norm_spinBox_16:
    }

}