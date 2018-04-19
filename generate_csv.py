# -*- coding: utf-8 -*-
# @Author: xiaodong
# @Date:   just hide
# @Last Modified by:   xiaodong
# @Last Modified time: just hide
import os
import traceback

import pandas as pd

def to_csv(frame: pd.core.frame.DataFrame,
            *,
           name: str):

    save_name = '{}.csv'.format(name)
    if not os.path.exists(save_name):
        try:
            frame.to_csv(save_name, encoding='utf-8', index=False)
            print('{}保存成功！'.format(name))
        except Exception as e:
            print('{}保存失败!'.format(name))
            traceback.print_exc()
    else:
        print('{}已存在'.format(name))

