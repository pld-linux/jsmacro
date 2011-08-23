Summary:	jsmacro - an oddly named JavaScript preprocessor
Name:		jsmacro
Version:	0.2.3
Release:	0.1
License:	MIT
Group:		Development/Languages/Python
Source0:	https://github.com/smartt/jsmacro/tarball/master#/%{name}-%{version}.tgz
# Source0-md5:	3df081110299ec7b4254b62249fc0229
URL:		http://www.eriksmartt.com/blog/archives/tag/jsmacro
BuildRequires:	rpmbuild(macros) >= 1.219
Requires:	python-hashlib
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
jsmacro is pre-processor designed for use with JavaScript

This tool was developed to meet a desire to strip Debug and Test code
from production JavaScript files in an automated manner.

%prep
%setup -qc
mv *-%{name}-*/* .

# fix #!%{_bindir}/env python -> #!%{__python}:
%{__sed} -i -e '1s,^#!.*python,#!%{__python},' %{name}.py

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
cp -p %{name}.py $RPM_BUILD_ROOT%{_bindir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE.txt README.markdown
%attr(755,root,root) %{_bindir}/jsmacro