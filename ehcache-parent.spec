%{?_javapackages_macros:%_javapackages_macros}
Name:          ehcache-parent
Version:       2.3
Release:       8.3
Summary:       Ehcache Parent
Group:         Development/Java
License:       ASL 2.0
URL:           https://www.terracotta.org/
# svn export http://svn.terracotta.org/svn/ehcache/tags/ehcache-parent-2.3
# tar czf ehcache-parent-2.3-src-svn.tar.gz ehcache-parent-2.3
Source0:       ehcache-parent-2.3-src-svn.tar.gz
BuildRequires: java-devel
BuildRequires: jpackage-utils
BuildRequires: maven-compiler-plugin
BuildRequires: maven-gpg-plugin
BuildRequires: maven-idea-plugin
BuildRequires: maven-javadoc-plugin
BuildRequires: maven-plugin-cobertura
BuildRequires: maven-pmd-plugin
BuildRequires: maven-source-plugin
BuildRequires: maven-release-plugin
BuildRequires: maven-surefire-plugin
Requires: jpackage-utils
Requires: java
BuildArch: noarch


%description
Ehcache is a widely used, pure Java, in-process, distributed cache.

%prep

%setup -q -n ehcache-parent-%{version}

%build

%install
install -d -m 755 $RPM_BUILD_ROOT%{_mavenpomdir}
install -pm 644 pom.xml $RPM_BUILD_ROOT%{_mavenpomdir}/JPP-%{name}.pom
%add_maven_depmap JPP-%{name}.pom


%files -f .mfiles

%changelog
* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jan 18 2012 David Nalley <david@gnsa.us> - 2.3-2
- removing antiquated maven2 stylings
- fixing BR so this actually builds. 

* Mon Jan 16 2012 David Nalley <david@gnsa.us> - 2.3-1 
- Initial rpm build - spec modified from mageia's version of same
