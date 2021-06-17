# 根据datastoreid 来获取datastore的名字
# 例子后面get-view -property name 用法比较重要，power-cli有很多根据id来获取name的情况，基本都可以用这个例子来解决，避免直接获取name带来的性能问题
Get-VM -Location "可选-指定datacenter" -Name "可选-指定vm" | % { @{$_.Name=$_.DatastoreIDList | %{(Get-View -Property Name -Id $_).Name}} }
