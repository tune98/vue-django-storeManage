# Generated by Django 2.2.5 on 2019-12-28 07:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CdDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cd_num', models.IntegerField(verbose_name='物料数量')),
                ('cd_taxRate', models.IntegerField(default=13, verbose_name='税率')),
                ('cd_tax_unitPrice', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='含税单价')),
                ('cd_unitPrice', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='无税单价')),
                ('cd_tax_sum', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='含税总额')),
                ('cd_sum', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='无税总额')),
                ('cd_rp_iden', models.CharField(max_length=15, verbose_name='请购单编号')),
                ('cd_rpd_remarks', models.TextField(max_length=400, verbose_name='物料备注')),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='material_cd', to='base.Material', verbose_name='物料')),
            ],
            options={
                'verbose_name': '合同物料明细',
            },
        ),
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('sta_iden', models.CharField(max_length=15, primary_key=True, serialize=False, verbose_name='库存盘点单编号')),
                ('sta_ware_house_iden', models.CharField(max_length=6, verbose_name='库存盘点仓库编码')),
                ('sta_date', models.DateTimeField(auto_now_add=True, verbose_name='库存盘点日期')),
                ('sta_status', models.IntegerField(choices=[(0, '草稿'), (1, '已审批')], verbose_name='库存盘点状态')),
                ('sta_creator', models.CharField(max_length=20, verbose_name='库存盘点单创建者')),
                ('sta_createDate', models.DateTimeField(auto_now_add=True, verbose_name='库存盘点单创建时间')),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orga_sta', to='base.Origanization', verbose_name='组织')),
            ],
            options={
                'verbose_name': '库存盘点单',
            },
        ),
        migrations.CreateModel(
            name='MaterialSo',
            fields=[
                ('mso_iden', models.CharField(max_length=15, primary_key=True, serialize=False, verbose_name='出库单编号')),
                ('mso_type', models.IntegerField(choices=[(0, '内部出库'), (1, '外部出库')], verbose_name='材料出库类型')),
                ('deliver_ware_house_iden', models.CharField(max_length=6, verbose_name='出库仓库编码')),
                ('mso_date', models.DateField(auto_now_add=True, verbose_name='材料出库日期')),
                ('mso_remarks', models.TextField(max_length=400, verbose_name='材料出库备注')),
                ('mso_status', models.IntegerField(choices=[(0, '草稿'), (1, '已审批')], verbose_name='材料出库单状态')),
                ('mso_creator', models.CharField(max_length=20, verbose_name='材料出库单创建人')),
                ('mso_createDate', models.DateTimeField(auto_now_add=True, verbose_name='材料出库单创建日期')),
                ('mso_req_department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.Department', verbose_name='申请部门')),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orga_mso', to='base.Origanization', verbose_name='组织')),
            ],
            options={
                'verbose_name': '材料出库单',
            },
        ),
        migrations.CreateModel(
            name='PurchaseContract',
            fields=[
                ('pc_iden', models.CharField(max_length=15, primary_key=True, serialize=False, verbose_name='合同编号')),
                ('pc_name', models.CharField(max_length=20, verbose_name='合同名称')),
                ('pc_date', models.DateTimeField(auto_now_add=True, verbose_name='合同签订日期')),
                ('pc_sum', models.IntegerField(verbose_name='合同总额')),
                ('pc_remarks', models.TextField(max_length=400, verbose_name='合同备注')),
                ('pc_status', models.IntegerField(choices=[(0, '草稿'), (1, '已审批')], verbose_name='合同状态')),
                ('pc_creator', models.CharField(max_length=20, verbose_name='合同创建者')),
                ('pc_createDate', models.DateTimeField(auto_now_add=True, verbose_name='合同创建时间')),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orga_pc', to='base.Origanization', verbose_name='组织')),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='supplier_pc', to='base.Supplier', verbose_name='供应商')),
            ],
            options={
                'verbose_name': '采购合同',
            },
        ),
        migrations.CreateModel(
            name='SellOrder',
            fields=[
                ('so_iden', models.CharField(max_length=15, primary_key=True, serialize=False, verbose_name='销售订单编号')),
                ('so_type', models.IntegerField(choices=[(0, '普通发票'), (1, '退换货')], verbose_name='订单类型')),
                ('so_date', models.DateField(auto_now_add=True, verbose_name='订单日期')),
                ('deliver_ware_house_iden', models.CharField(max_length=6, verbose_name='发货仓库编码')),
                ('so_remarks', models.TextField(max_length=400, verbose_name='订单备注')),
                ('so_status', models.IntegerField(choices=[(0, '草稿'), (1, '已审批')], verbose_name='销售订单状态')),
                ('so_creator', models.CharField(max_length=20, verbose_name='订单创建人')),
                ('so_createDate', models.DateTimeField(auto_now_add=True, verbose_name='订单创建日期')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customer_so', to='base.Customer', verbose_name='客户')),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orga_so', to='base.Origanization', verbose_name='组织')),
            ],
        ),
        migrations.CreateModel(
            name='TransferRequest',
            fields=[
                ('str_iden', models.CharField(max_length=15, primary_key=True, serialize=False, verbose_name='转库申请单编号')),
                ('str_to_house', models.CharField(max_length=6, verbose_name='转入仓库编码')),
                ('str_from_house', models.CharField(max_length=6, verbose_name='转出仓库编码')),
                ('str_date', models.DateField(auto_now_add=True, verbose_name='转库申请日期')),
                ('str_status', models.IntegerField(choices=[(0, '草稿'), (1, '已审批')], verbose_name='转库申请单状态')),
                ('str_creator', models.CharField(max_length=20, verbose_name='销售出库单创建人')),
                ('str_createDate', models.DateTimeField(auto_now_add=True, verbose_name='销售出库单创建日期')),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orga_str', to='base.Origanization', verbose_name='组织')),
            ],
            options={
                'verbose_name': '转库申请单',
            },
        ),
        migrations.CreateModel(
            name='TrDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trd_num', models.IntegerField(verbose_name='转库申请数量')),
                ('trd_present_num', models.IntegerField(verbose_name='材料现存量')),
                ('trd_remarks', models.TextField(max_length=400, verbose_name='转库单明细备注')),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='material_trd', to='base.Material', verbose_name='物料')),
                ('transfer_request', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='str_trd', to='orderManage.TransferRequest', verbose_name='转库申请单')),
            ],
            options={
                'verbose_name': '转库申请单详情',
            },
        ),
        migrations.CreateModel(
            name='Transfer',
            fields=[
                ('st_iden', models.CharField(max_length=15, primary_key=True, serialize=False, verbose_name='转库单编号')),
                ('st_date', models.DateField(auto_now_add=True, verbose_name='转库日期')),
                ('st_status', models.IntegerField(choices=[(0, '草稿'), (1, '已审批')], verbose_name='转库单状态')),
                ('st_creator', models.CharField(max_length=20, verbose_name='转库单创建者')),
                ('st_createDate', models.DateTimeField(auto_now_add=True, verbose_name='转库单创建时间')),
                ('transfer_request', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='orderManage.TransferRequest', verbose_name='转库申请单')),
            ],
            options={
                'verbose_name': '转库单',
            },
        ),
        migrations.CreateModel(
            name='StDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('td_real_num', models.IntegerField(verbose_name='转库实发数量')),
                ('td_present_num', models.IntegerField(verbose_name='材料现存量')),
                ('td_remarks', models.TextField(max_length=400, verbose_name='转库单明细备注')),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='material_td', to='base.Material', verbose_name='物料')),
                ('transfer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='st_td', to='orderManage.Transfer', verbose_name='转库单')),
            ],
            options={
                'verbose_name': '转库单明细',
            },
        ),
        migrations.CreateModel(
            name='StaDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sd_paper_num', models.IntegerField(verbose_name='账面数量')),
                ('sd_real_num', models.IntegerField(verbose_name='盘点数量')),
                ('sd_diff_num', models.IntegerField(verbose_name='差异数量')),
                ('sd_adjm_price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='调整单价')),
                ('sd_adjm_sum', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='调整金额')),
                ('sd_remarks', models.TextField(max_length=400, verbose_name='库存盘点明细备注')),
                ('inventory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sta_sd', to='orderManage.Inventory', verbose_name='库存盘点单')),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='material_sd', to='base.Material', verbose_name='物料')),
            ],
            options={
                'verbose_name': '库存盘明细',
            },
        ),
        migrations.CreateModel(
            name='SoDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sod_num', models.IntegerField(verbose_name='销售数量')),
                ('sod_taxRate', models.IntegerField(default=13, verbose_name='税率')),
                ('sod_tax_unitPrice', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='含税单价')),
                ('sod_unitPrice', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='无税单价')),
                ('sod_tax_sum', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='含税总额')),
                ('sod_sum', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='无税总额')),
                ('sod_tax_price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='税金总额')),
                ('sod_remarks', models.TextField(max_length=200, verbose_name='订单明细备注')),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='material_sod', to='base.Material', verbose_name='物料')),
                ('sell_order', models.ForeignKey(on_delete=models.Model, related_name='so_sod', to='orderManage.SellOrder', verbose_name='销售订单')),
            ],
            options={
                'verbose_name': '销售订单明细',
            },
        ),
        migrations.CreateModel(
            name='SellSo',
            fields=[
                ('sso_iden', models.CharField(max_length=15, primary_key=True, serialize=False, verbose_name='销售出库单编号')),
                ('sso_status', models.IntegerField(choices=[(0, '草稿'), (1, '已审批')], verbose_name='销售出库单状态')),
                ('sso_creator', models.CharField(max_length=20, verbose_name='销售出库单创建人')),
                ('sso_createDate', models.DateTimeField(auto_now_add=True, verbose_name='销售出库单创建日期')),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orga_sso', to='base.Origanization', verbose_name='组织')),
                ('sell_order', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='orderManage.SellOrder', verbose_name='销售订单')),
            ],
            options={
                'verbose_name': '销售出库单明细',
            },
        ),
        migrations.CreateModel(
            name='PurchaseRequest',
            fields=[
                ('pr_iden', models.CharField(max_length=15, primary_key=True, serialize=False, verbose_name='请购单编号')),
                ('pr_department', models.CharField(max_length=20, verbose_name='请购部门')),
                ('pr_date', models.DateTimeField(auto_now_add=True, verbose_name='请购日期')),
                ('pr_remarks', models.TextField(max_length=400, verbose_name='请购备注')),
                ('pr_status', models.IntegerField(choices=[(0, '草稿'), (1, '已审批'), (2, '已关闭')], verbose_name='请购状态')),
                ('pr_creator', models.CharField(max_length=20, verbose_name='请购创建者')),
                ('pr_createDate', models.DateTimeField(auto_now_add=True, verbose_name='请购创建时间')),
                ('pr_closer', models.CharField(max_length=20, verbose_name='请购关闭者')),
                ('pr_closeDate', models.DateTimeField(auto_now_add=True, verbose_name='请购关闭时间')),
                ('pr_closeReason', models.TextField(max_length=200, verbose_name='请购关闭原因')),
                ('material_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.MaterialType', verbose_name='物料类别')),
                ('origanization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orga_pr', to='base.Origanization', verbose_name='组织')),
            ],
            options={
                'verbose_name': '请购单',
            },
        ),
        migrations.CreateModel(
            name='PurchaseOrder',
            fields=[
                ('po_iden', models.CharField(max_length=15, primary_key=True, serialize=False, verbose_name='采购订单编号')),
                ('po_date', models.DateTimeField(auto_now_add=True, verbose_name='采购订单生效日期')),
                ('po_sum', models.IntegerField(verbose_name='采购订单总额')),
                ('po_remarks', models.TextField(max_length=400, verbose_name='采购订单备注')),
                ('po_status', models.IntegerField(choices=[(0, '草稿'), (1, '已审批')], verbose_name='采购订单状态')),
                ('po_creator', models.CharField(max_length=20, verbose_name='采购订单创建者')),
                ('po_createDate', models.DateTimeField(auto_now_add=True, verbose_name='采购订单创建时间')),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orga_po', to='base.Origanization', verbose_name='组织')),
                ('purchase_contract', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pc_po', to='orderManage.PurchaseContract', verbose_name='采购合同')),
                ('purchase_request', models.ForeignKey(on_delete=models.Model, related_name='pr_po', to='orderManage.PurchaseRequest', verbose_name='请购单')),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='supplier_po', to='base.Supplier', verbose_name='供应商')),
            ],
            options={
                'verbose_name': '采购订单',
            },
        ),
        migrations.CreateModel(
            name='PrDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prd_num', models.IntegerField(verbose_name='请购数量')),
                ('prd_remarks', models.TextField(max_length=400, verbose_name='物料请购备注')),
                ('prd_used', models.IntegerField(choices=[(0, '未使用'), (1, '已使用')], verbose_name='明细单是否使用')),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='material_prd', to='base.Material', verbose_name='物料')),
                ('purchase_request', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pr_prd', to='orderManage.PurchaseRequest', verbose_name='请购单')),
            ],
            options={
                'verbose_name': '请购单物料明细',
            },
        ),
        migrations.CreateModel(
            name='OtherSo',
            fields=[
                ('oso_iden', models.CharField(max_length=15, primary_key=True, serialize=False, verbose_name='其它出库单编号')),
                ('oso_type', models.IntegerField(choices=[(0, '转库出库'), (1, '盘亏出库')], verbose_name='其它出库单类型')),
                ('oso_date', models.DateField(auto_now_add=True, verbose_name='其它出库日期')),
                ('oso_remarks', models.TextField(max_length=400, verbose_name='其它出库单备注')),
                ('oso_form_iden', models.CharField(max_length=15, verbose_name='来源单号')),
                ('oso_status', models.IntegerField(choices=[(0, '草稿'), (1, '已审批')], verbose_name='其它出库单状态')),
                ('oso_creator', models.CharField(max_length=20, verbose_name='其它出库单创建人')),
                ('oso_createDate', models.DateTimeField(auto_now_add=True, verbose_name='其它出库单创建日期')),
                ('inventory', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='orderManage.Inventory', verbose_name='库存盘点单')),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orga_oso', to='base.Origanization', verbose_name='组织')),
                ('transfer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='orderManage.Transfer', verbose_name='转库单')),
            ],
            options={
                'verbose_name': '其它出库单',
            },
        ),
        migrations.CreateModel(
            name='OtherSi',
            fields=[
                ('osi_iden', models.CharField(max_length=15, primary_key=True, serialize=False, verbose_name='其它入库单编号')),
                ('osi_house', models.CharField(max_length=15, verbose_name='其它入库仓库编号')),
                ('osi_type', models.IntegerField(choices=[(0, '转库入库'), (1, '盘盈出库')], verbose_name='其它入库单类型')),
                ('osi_date', models.DateField(auto_now_add=True, verbose_name='其它出库日期')),
                ('osi_remarks', models.TextField(max_length=400, verbose_name='其它出库单备注')),
                ('osi_status', models.IntegerField(choices=[(0, '草稿'), (1, '已审批')], verbose_name='其它出库单状态')),
                ('osi_creator', models.CharField(max_length=20, verbose_name='其它出库单创建人')),
                ('osi_createDate', models.DateTimeField(auto_now_add=True, verbose_name='其它出库单创建日期')),
                ('inventory', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='orderManage.Inventory', verbose_name='库存盘点单')),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orga_osi', to='base.Origanization', verbose_name='组织')),
                ('transfer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='orderManage.Transfer', verbose_name='转库单')),
            ],
            options={
                'verbose_name': '其它出库单',
            },
        ),
        migrations.CreateModel(
            name='OsoDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('osod_num', models.IntegerField(verbose_name='其它出库物料数量')),
                ('osod_remarks', models.TextField(max_length=400, verbose_name='其它出库物料明细')),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='material_osod', to='base.Material', verbose_name='物料')),
                ('other_so', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='oso_osod', to='orderManage.OtherSo', verbose_name='其它出库单')),
            ],
            options={
                'verbose_name': '其它出库单明细',
            },
        ),
        migrations.CreateModel(
            name='OsiDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('osid_paper_num', models.IntegerField(verbose_name='应收数量')),
                ('osid_real_num', models.IntegerField(verbose_name='实收数量')),
                ('osid_price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='无税单价')),
                ('osid_sum', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='无税总额')),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='material_osid', to='base.Material', verbose_name='物料')),
                ('other_si', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='osi_osid', to='orderManage.OtherSi', verbose_name='其它入库单')),
            ],
        ),
        migrations.CreateModel(
            name='OrDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('od_num', models.IntegerField(verbose_name='采购数量')),
                ('od_taxRate', models.IntegerField(default=13, verbose_name='税率')),
                ('od_tax_unitPrice', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='含税单价')),
                ('od_unitPrice', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='无税单价')),
                ('od_tax_sum', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='含税总额')),
                ('od_sum', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='无税总额')),
                ('od_rp_iden', models.CharField(max_length=15, verbose_name='请购单编号')),
                ('od_rpd_remarks', models.TextField(max_length=400, verbose_name='物料备注')),
                ('cd_detail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cd_od', to='orderManage.CdDetail', verbose_name='合同物料明细')),
                ('pr_detail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pr_od', to='orderManage.PrDetail', verbose_name='请购单物料明细')),
                ('purchase_contract', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pc_od', to='orderManage.PurchaseContract', verbose_name='采购合同')),
            ],
            options={
                'verbose_name': '采购订单详情',
            },
        ),
        migrations.CreateModel(
            name='OpeningInventory',
            fields=[
                ('oi_iden', models.CharField(max_length=15, primary_key=True, serialize=False, verbose_name='期初库存单编号')),
                ('oi_ware_house_iden', models.CharField(max_length=6, verbose_name='期初库存盘点仓库编码')),
                ('oi_date', models.DateTimeField(auto_now_add=True, verbose_name='期初库存盘点日期')),
                ('oi_status', models.IntegerField(choices=[(0, '草稿'), (1, '已审批')], verbose_name='期初库存盘点状态')),
                ('oi_creator', models.CharField(max_length=20, verbose_name='期初库存盘点单创建者')),
                ('oi_createDate', models.DateTimeField(auto_now_add=True, verbose_name='期初库存盘点单创建时间')),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orga_oi', to='base.Origanization', verbose_name='组织')),
            ],
            options={
                'verbose_name': '期初库存盘点单',
            },
        ),
        migrations.CreateModel(
            name='OiDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('oid_num', models.IntegerField(verbose_name='入库数量')),
                ('oid_price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='入库单价')),
                ('oid_sum', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='入库总价')),
                ('oid_date', models.DateTimeField(auto_now_add=True, verbose_name='入库时间')),
                ('oid_remarks', models.TextField(max_length=400, verbose_name='期初库存盘点明细备注')),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='material_oid', to='base.Material', verbose_name='物料')),
                ('opening_inventory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='oi_oid', to='orderManage.OpeningInventory', verbose_name='期初库存盘点')),
            ],
            options={
                'verbose_name': '期初库存盘点明细',
            },
        ),
        migrations.CreateModel(
            name='MsoDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('msod_num', models.IntegerField(verbose_name='材料出库数量')),
                ('msod_present_num', models.IntegerField(verbose_name='材料现存量')),
                ('msod_remarks', models.TextField(max_length=200, verbose_name='材料出库单明细备注')),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='material_msod', to='base.Material', verbose_name='物料')),
                ('material_so', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mso_msod', to='orderManage.MaterialSo', verbose_name='材料出库单')),
            ],
            options={
                'verbose_name': '材料出库单明细',
            },
        ),
        migrations.CreateModel(
            name='CdPayDetail',
            fields=[
                ('pay_batch', models.IntegerField(primary_key=True, serialize=False, verbose_name='付款批次')),
                ('pay_rate', models.IntegerField(verbose_name='付款比率')),
                ('pay_price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='付款金额')),
                ('pay_planDate', models.DateField(verbose_name='计划付款日期')),
                ('pay_preay', models.IntegerField(choices=[(0, '是'), (1, '否')], verbose_name='是否预付款')),
                ('pay_remarks', models.TextField(max_length=400, verbose_name='付款备注')),
                ('purchase_contract', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pc_pay', to='orderManage.PurchaseContract', verbose_name='采购合同')),
            ],
            options={
                'verbose_name': '合同付款协议',
            },
        ),
        migrations.AddField(
            model_name='cddetail',
            name='purchase_contract',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pc_cd', to='orderManage.PurchaseContract', verbose_name='采购合同'),
        ),
        migrations.CreateModel(
            name='BuyInStore',
            fields=[
                ('bis_iden', models.CharField(max_length=15, primary_key=True, serialize=False, verbose_name='入库单编号')),
                ('bis_date', models.DateField(auto_now_add=True, verbose_name='采购入库日期')),
                ('bis_remarks', models.TextField(max_length=400, verbose_name='采购入库单备注')),
                ('bis_status', models.IntegerField(choices=[(0, '草稿'), (1, '已审批')], verbose_name='采购入库单状态')),
                ('bis_creator', models.CharField(max_length=20, verbose_name='采购入库单创建人')),
                ('bis_createDate', models.DateTimeField(auto_now_add=True, verbose_name='采购入库单创建日期')),
                ('origanization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orga_bis', to='base.Origanization', verbose_name='组织')),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='supplier_bis', to='base.Supplier', verbose_name='供应商')),
                ('totalwarehouse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='total_ware_house_bis', to='base.TotalWareHouse', verbose_name='总仓')),
            ],
            options={
                'verbose_name': '材料出库单',
            },
        ),
        migrations.CreateModel(
            name='BisDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bd_paper_num', models.IntegerField(verbose_name='应入库数量')),
                ('bd_real_num', models.IntegerField(verbose_name='实际入库数量')),
                ('bd_unitPrice', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='无税单价')),
                ('bd_sum', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='无税总额')),
                ('po_iden', models.CharField(max_length=15, verbose_name='采购订单号')),
                ('pr_iden', models.CharField(max_length=15, verbose_name='请购订单号')),
                ('buy_in_store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mso_bd', to='orderManage.MaterialSo', verbose_name='材料出库单')),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='material_bd', to='base.Material', verbose_name='物料')),
            ],
            options={
                'verbose_name': '采购入库单明细',
            },
        ),
    ]