# 导入powershellC模块
# Import-Module -Name "Initialize-PowerCLIEnvironment.ps1" | Out-Null
# Out-Null 忽略提示信息
Import-Module -Name <PowerCLI路径> | Out-Null
Import-Module Microsoft.PowerShell.Utility | Out-Null

# 连接vmware 
Connect-VIServer <vCenterIP地址> -Username <用户名> -Password <密码> | Out-Null

# 查看vm宿主机信息
# $vmware_info = Get-Vmhost

# 定义空字符串
$collect_info=""

# 查询vm宿主机的Name信息
# 使用select参数，仅显示Name列对应的数据
$vmware_hostinfo = (Get-Vmhost | select).Name
# 查询vm宿主机对应的版本号
$vmware_versioninfo = (Get-Vmhost | select).Version

# for循环进行格式化数据
# $vmware_hostinfo.count：统计数据行数，类似linux的wc -l命令
for ($i=1;$i -lt $vmare_hostinfo.count; $i++) {
    # 根据下标去对应的数据值
    $collect_info += "name:" + $vmare_hostinfo[$i] + ",version:" + $vmware_versioninfo[$i] 
}

# 输出采集后的数据
echo -n $collect_info.Trim(" .-`t`n`r")